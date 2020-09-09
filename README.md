# light-koreanbots
## (비공식 모듈)
공식 SDK가 너무 무거운가요? 그냥 서버수 업데이트만 하면 되나요? 그러면 이 모듈을 사용해보세요!  

## 기능
서버수 자동 업데이트  
**이 외의 기능은 추가할 생각이 없습니다**

## 예제
```pydocstring
import light_koreanbots as lkb
import discord

client = discord.Client()
kbot_token = "koreanbots_token"
lkb_client = lkb.LKBClient(bot=client, token=kbot_token)

client.run("discord_token")
```