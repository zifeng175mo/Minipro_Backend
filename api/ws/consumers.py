import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncJsonWebsocketConsumer, AsyncWebsocketConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):
    chats = dict()

    async def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        # 将用户添加至聊天组信息chats中
        try:
            ChatConsumer.chats[self.group_name].add(self)
        except:
            ChatConsumer.chats[self.group_name] = {self}
        # print(ChatConsumer.chats)
        # 创建连接时调用
        await self.accept()

    async def disconnect(self, close_code):
        # 连接关闭时调用
        # 将关闭的连接从群组中移除
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        # 将该客户端移除聊天组连接信息
        ChatConsumer.chats[self.group_name].remove(self)
        await self.close()

    async def receive_json(self, message, **kwargs):
        # 收到信息时调用
        print(message)
        # 信息发送
        length = len(ChatConsumer.chats[self.group_name])
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat.message',
                'user_name': message.get('user_name'),
                'user_id': message.get('user_id'),
                'content': message.get('content'),
                'time': message.get('time')
            },
        )

    async def chat_message(self, event):
        # Handles the 'chat.message' event when it's sent to us.
        await self.send_json({
            'user_name': event['user_name'],
            'user_id': event['user_id'],
            'content': event['content'],
            'time': event['time']
        })


# 推送consumer
class PushConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['username']

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

        # print(PushConsumer.chats)

    async def push_message(self, event):
        print(event)
        await self.send(text_data=json.dumps({
            'event': event['event']
        }))
