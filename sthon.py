import telethon
from telethon import Button
from telethon.tl.functions.channels import LeaveChannelRequest
import os
from config import *
import logging
import asyncio
import time
from time import sleep
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
import random
bilal.start()
a = requests.session()
bot_username = '@eeobot'
bot_username1 = '@A_MAN9300BOT'
bot_username2 = '@MARKTEBOT'
bot_username3 = '@xnsex21bot'
bot_username4='@Burllionbot'
bot_username5='@cn2bot'
bot_username6='@ihyberbot'
bot_username7='@YY8BoT'
LOGS = logging.getLogger(__name__)
DEVS = [6066647930]
onerbilal_id = (int(DEVLOO))
@bilal.on(events.NewMessage(outgoing=False,pattern='.الاوامر'))
async def onerstart(event):
	sender = await event.get_sender()
	if sender.id == onerbilal_id:
		order = await event.reply('''
		**مرحبا بك في اوامر سورس شهم 
===== 𝐒𝐇𝐀𝐇𝐌 ======
𝟏 - للدخول الى اوامر التجميع :.التجميع
𝟐 - للدخول الى اوامر التحـكم : .التحكم
𝟑 - للدخول الى اوامر مـمـيـزة : .المميزة
𝟒 - لـفـحص عـمـل الـســورس : .فحص
=====	𝐒𝐇𝐀𝐇𝐌 =====		''')
@bilal.on(events.NewMessage)
async def join_channel(event):
	try :
		await bilal(JoinChannelRequest('@SHA_HM1'))
	except BaseException:
		pass		
@bilal.on(events.NewMessage)
async def join_channel(event):
	try:
		await bilal(JoinChannelRequest('@SHA_HM2'))
	except BaseException :
		pass
@bilal.on(events.NewMessage)
async def join_channel(event):
	try:
		await bilal(JoinChannelRequest('@Super_Shahm'))
	except BaseException :
		pass

@bilal.on(events.NewMessage)
async def join_channel(event):
	try:
		await bilal(JoinChannelRequest('@SH_AH_M1'))
	except BaseException :
		pass
@bilal.on(events.NewMessage(outgoing=False, pattern='.فحص'))
async def onerstart(event):
	sender = await event.get_sender()
	if sender.id == onerbilal_id:
		order = await event.reply('السورس يعمل بنجاح حبيبي ')
@bilal.on(events.NewMessage(outgoing=True,pattern='.فحص'))
async def ms(event):
		
		await event.edit(f'''السورس يعمل بنجاح قم بارسال ( .الاوامر ) ''')
@bilal.on(events.NewMessage(outgoing=True,pattern='.الاوامر'))
async def ms (event):
		await event.edit("""**
〠 اوامر حساب المستخدم 
• بوت تمويل المليار  - `.تجميع المليار`
• بوت تمويل الجوكر - `.تجميع الجوكر`
• بوت تمويل العقـاب - `.تجميع العقاب`
• بوت تمويل العـرب  - `.تجميع العرب 
• بوت تمويل برليون  - `.تجميع برليون`
• بوت تمويل اسيا - `.تجميع اسيا`
• بوت تمويل هايبر - `.تجميع هايبر`
• بوت تمويل السلطان  - `.تجميع السلطان` 
• فحص السورس      - `.فحص`**""")
@bilal.on(events.NewMessage(outgoing=False , pattern='.التجميع'))
async def onerstart(event):
		sender = await event.get_sender()
		if sender.id==onerbilal_id:
			order = await event.reply("""**


⚝ قـائمة جميع اوامر التجميع التي تحتاجها
====== 𝐒𝐇𝐀𝐇𝐌 ======
`.المليار` :  تجميع نقاط بوت المليار
`.الجوكر` : تجميع نقاط بوت الجوكر 
`.العقاب` :  تجميع نقاط بوت العقاب 
`.العرب` :   تجميع نقاط بوت العرب
`.برليون` :   تجميع نقاط بوت برليون
`.اسيا` :   تجميع نقاط بوت اسيا
`.هايبر` :   تجميع نقاط بوت هايبر
`.السلطان` :   تجميع نقاط بوت السلطان


ملاحظة : تستخدم هذه الاوامر بأرسالها الى الحساب او بأرسالها الى مجموعة يوجد فيها الحساب
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
`.بوت + يوزر البوت` : تجميع نقاط بوت غير موجود في القائمة
ملاحظة : يوزر البوت المطلوب هو البوت المراد التجميع فيهـ
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
`.لانهائي +يوزر البوت + عدد الثواني` : تجميع لانهائي 
ملاحظة : يوزر البوت المطلوب المراد التجميع فيهـ 
ملاحظة : عدد الثواني هو العدد الذي سيكون الفاصل بين كل محاولة تجميع نقاط 
ملاحظة : ننصحك بوضع عدد الثواني 3600
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
`.انضمام` : الانضمام الى قنوات البوتات المذكورة
`.التحويل` : الدخول لقائمة تحويل نقاط
`.معلومات` : الدخول لقائمة تحويل معلومات
`.مغادرة القنواة` : لمغادرة جميع القنوات والمجموعات
`.الهدية +يوزر البوت`: لتجميع الهدية من البوت المرسل
====== 𝐒𝐇𝐀𝐇𝐌 ======
**""")
@bilal.on(events.NewMessage(outgoing=False,pattern='.التحكم'))
async def onerstart(event):
	sender= await event.get_sender()
	if sender.id== onerbilal_id:
		order = await event.reply("""**
⚝ قائمة اوامر التحكم بالحساب
====== 𝐒𝐇𝐀𝐇𝐌 ======
𝟏 - لتحويل اخر رسالة من مستخدم معين او بوت :
`.جلب + يوزر الحساب او البوت`
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
𝟐 - لأرسال رسالة الى مستخدم معين او بوت : 
`.ارسل+ الرسالة + يوزر الحساب او البوت`
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
𝟑 - لجعل الحساب ينقر على زر شفاف في بوت : 
`.زر+ رقم الزر الشفاف + يوزر البوت`
ملاحظة :  قم بحساب رقم الزر الشفاف من العدد 0
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
𝟒 - لجعل الحساب ينضم الى قناة او مجموعة
`.انضم+ يوزر القناة او المجموعة `
====== 𝐒𝐇𝐀𝐇𝐌 ======
**""")
@bilal.on(events.NewMessage(outgoing=False , pattern='.المميزة'))
async def onerstart(event):
	sender= await event.get_sender()
	if sender.id == onerbilal_id:
		order = await event.reply("""**
⚝ قائمة الاوامر المميزة 
===== 𝐒𝐇𝐀𝐇𝐌 =====
𝟏 - لتفعيل بوت عبر الدخول الى رابط الدعوه : 
`.تفعيل + ايدي الحساب + يوزر البوت`
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
𝟐 - الامر التالي يحتوي على ملاحظات تحتاجها :
`/ملاحظة`
𝟑 - لجعل الحساب يصوت في مسابقة لايكات :
`.صوت+ موقع الرسالة + يوزر القناة`
ملاحظة : موقع الرسالة يعني مثلا اذا كان الاسم في قناة المسابقة اخر اسم او اخر منشور فأن موقع الرسالة 1 وان تكن قبل الاخير فأن موقها 2 وهكذا  بقية المواقع 
𝟒 - لجعل الحساب يغادر قناة او مجموعة :
`.غادر+ يوزر القناة`
====== 𝐒𝐇𝐀𝐇𝐌 ======
**""")
@bilal.on(events.NewMessage(outgoing=False, pattern='.ملاحظة'))
async def onerstart(event):
	sender =  await event.get_sender()
	if sender.id == onerbilal_id:
		order = await event.reply("""**
1 - اذا كنت تريد التحكم بالحسابات في التحميع وتحويل النقاط ومعرفة معلومات كل حساب قم بأنشاء مجموعة خاصة وادخل الحسابات التي قمت بتنصيب لها السورس وارفع الحسابات الى مشرفين ثم استخدم اوامر التجميع 
2 - اذا كنت تريد جعل الحسابات تقوم بتجميع النقاط بدون توقف ونسبة قليلة من الحظر استخدم الامر : .لانهائي 
بأمكانك معرفة المزيد عن الامر وكيفية استخدامه في قائمة .تجميع ويستحسن عند استعمال الامر وضع عدد الثواني 300 اي يعني هذا عند حدوث خطأ في التجميع او انتهت القنوات فسوف يقوم السورس بالمحاولة في التجميع تلقائيا بعد مرور 300 اي خمس دقائق وسوف يقوم السورس بأخبارك جميع ماتم الوصول اليه من الامر ويمكنك ايقاف التجميع بأرسال .اعادة تشغيل 
3 - اذا كنت تريد تجميع نقاط بوتات التمويل بطريقة اعتيادية بدون المحاولة مرة اخرى تلقائيا يمكن استخدام الاوامر التالية [.تجميع في المليار + .تجميع في الجوكر .......] يمكنك مراجعة الاوامر في القائمة .تجميع في اول قسمين من القائمة
**""")

@bilal.on(events.NewMessage(outgoing=False, pattern='.المليار'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await bilal(JoinChannelRequest('SHA_HM1'))
        channel_entity = await bilal.get_entity(bot_username)
        await bilal.send_message(bot_username, '/start')
        await asyncio.sleep(4)
        msg0 = await bilal.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await bilal.get_messages(bot_username, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await bilal(GetHistoryRequest(peer=channel_entity, limit=1,                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await shahm1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await bilal(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await bilal(ImportChatInviteRequest(bott))
                msg2 = await bilal.get_messages(bot_username, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await bilal.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await bilal.send_message(event.chat_id, "تم الانتهاء من التجميع | SH")

@bilal.on(events.NewMessage(outgoing=False, pattern='.الجوكر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await bilal(JoinChannelRequest('SHA_HM1'))
        channel_entity = await bilal.get_entity(bot_username1)
        await bilal.send_message(bot_username1, '/start')
        await asyncio.sleep(4)
        msg0 = await bilal.get_messages(bot_username1, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await bilal.get_messages(bot_username1, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await bilal(GetHistoryRequest(peer=channel_entity, limit=1,                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await bilal.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await bilal(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await bilal(ImportChatInviteRequest(bott))
                msg2 = await bilal.get_messages(bot_username1, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await bilal.get_messages(bot_username1, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await bilal.send_message(event.chat_id, "تم الانتهاء من التجميع | SH")

@bilal.on(events.NewMessage(outgoing=False, pattern='.العقاب'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await bilal(JoinChannelRequest('SHA_HM1'))
        channel_entity = await bilal.get_entity(bot_username2)
        await bilal.send_message(bot_username2, '/start')
        await asyncio.sleep(4)
        msg0 = await bilal.get_messages(bot_username2, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await bilal.get_messages(bot_username2, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await bilal(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await bilal.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await bilal(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await bilal(ImportChatInviteRequest(bott))
                msg2 = await bilal.get_messages(bot_username2, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await bilal.get_messages(bot_username2, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await bilal.send_message(event.chat_id, "تم الانتهاء من التجميع | SH")


@bilal.on(events.NewMessage(outgoing=False, pattern='.العرب'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await bilal(JoinChannelRequest('SHA_HM1'))
        channel_entity = await bilal.get_entity(bot_username3)
        await bilal.send_message(bot_username3, '/start')
        await asyncio.sleep(4)
        msg0 = await bilal.get_messages(bot_username3, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await bilal.get_messages(bot_username3, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await bilal(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await bilal.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await bilal(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await bilal(ImportChatInviteRequest(bott))
                msg2 = await bilal.get_messages(bot_username3, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await bilal.get_messages(bot_username3, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await bilal.send_message(event.chat_id, "تم الانتهاء من التجميع | SH")


@bilal.on(events.NewMessage(outgoing=False, pattern='.برليون'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await bilal(JoinChannelRequest('SHA_HM1'))
        channel_entity = await bilal.get_entity(bot_username4)
        await bilal.send_message(bot_username4, '/start')
        await asyncio.sleep(4)
        msg0 = await bilal.get_messages(bot_username4, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await bilal.get_messages(bot_username4, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await bilal(GetHistoryRequest(peer=channel_entity, limit=1,                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await shahm1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await bilal(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await bilal(ImportChatInviteRequest(bott))
                msg2 = await bilal.get_messages(bot_username4,limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await bilal.get_messages(bot_username4, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await bilal.send_message(event.chat_id, "تم الانتهاء من التجميع | SH")


@bilal.on(events.NewMessage(outgoing=False, pattern='.اسيا'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await bilal(JoinChannelRequest('SHA_HM1'))
        channel_entity = await bilal.get_entity(bot_username5)
        await bilal.send_message(bot_username5, '/start')
        await asyncio.sleep(4)
        msg0 = await bilal.get_messages(bot_username5, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await bilal.get_messages(bot_username5, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await bilal(GetHistoryRequest(peer=channel_entity, limit=1,                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await shahm1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await bilal(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await bilal(ImportChatInviteRequest(bott))
                msg2 = await bilal.get_messages(bot_username5,limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await bilal.get_messages(bot_username5, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await bilal.send_message(event.chat_id, "تم الانتهاء من التجميع | SH")

@bilal.on(events.NewMessage(outgoing=False, pattern='.هايبر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await bilal(JoinChannelRequest('SHA_HM1'))
        channel_entity = await bilal.get_entity(bot_username6)
        await bilal.send_message(bot_username6, '/start')
        await asyncio.sleep(4)
        msg0 = await bilal.get_messages(bot_username6, limit=1)
        await msg0[0].click(0)
        await asyncio.sleep(4)
        msg1 = await bilal.get_messages(bot_username6, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await bilal(GetHistoryRequest(peer=channel_entity, limit=1,                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await shahm1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await bilal(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await bilal(ImportChatInviteRequest(bott))
                msg2 = await bilal.get_messages(bot_username6, limit=1)
                await msg2[0].click(1)
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await bilal.get_messages(bot_username6, limit=1)
                await msg2[0].click(2)
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await bilal.send_message(event.chat_id, "تم الانتهاء من التجميع | SH")

@bilal.on(events.NewMessage(outgoing=False, pattern='.السلطان'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await bilal(JoinChannelRequest('SHA_HM1'))
        channel_entity = await bilal.get_entity(bot_username7)
        await bilal.send_message(bot_username7, '/start')
        await asyncio.sleep(4)
        msg0 = await bilal.get_messages(bot_username7, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await bilal.get_messages(bot_username7, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await bilal(GetHistoryRequest(peer=channel_entity, limit=1,                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await shahm1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await bilal(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await bilal(ImportChatInviteRequest(bott))
                msg2 = await bilal.get_messages(bot_username7,limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await bilal.get_messages(bot_username7, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await bilal.send_message(event.chat_id, "تم الانتهاء من التجميع | SH")
@bilal.on(events.NewMessage(outgoing=True, pattern='.تجميع المليار'))
async def OwnerStart(event):
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await bilal(JoinChannelRequest('SHA_HM1'))
        channel_entity = await bilal.get_entity(bot_username)
        await bilal.send_message(bot_username, '/start')
        await asyncio.sleep(4)
        msg0 = await bilal.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await bilal.get_messages(bot_username, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await bilal(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await shahm1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await bilal(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await bilal(ImportChatInviteRequest(bott))
                msg2 = await bilal.get_messages(bot_username, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await bilal.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await bilal.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH\nعدد النقاط المجموعة: {chs}")

@bilal.on(events.NewMessage(outgoing=True, pattern='.تجميع الجوكر'))
async def arab(event):
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await bilal(JoinChannelRequest('SHA_HM1'))
        channel_entity = await bilal.get_entity(bot_username1)
        await bilal.send_message(bot_username1, '/start')
        await asyncio.sleep(4)
        msg0 = await bilal.get_messages(bot_username1, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await bilal.get_messages(bot_username1, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await bilal(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await shahm1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await bilal(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await bilal(ImportChatInviteRequest(bott))
                msg2 = await bilal.get_messages(bot_username1, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await bilal.get_messages(bot_username1, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await bilal.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH\nعدد النقاط المجموعة: {chs}")

@bilal.on(events.NewMessage(outgoing=True, pattern='.تجميع العقاب'))
async def arab(event):
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await bilal(JoinChannelRequest('SHA_HM1'))
        channel_entity = await bilal.get_entity(bot_username2)
        await bilal.send_message(bot_username2, '/start')
        await asyncio.sleep(4)
        msg0 = await bilal.get_messages(bot_username2, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await bilal.get_messages(bot_username2, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await bilal(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await shahm1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await bilal(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await bilal(ImportChatInviteRequest(bott))
                msg2 = await bilal.get_messages(bot_username2, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await bilal.get_messages(bot_username2, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await bilal.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH\nعدد النقاط المجموعة: {chs}")

@bilal.on(events.NewMessage(outgoing=True, pattern='.تجميع العرب'))
async def arab(event):
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await bilal(JoinChannelRequest('SHA_HM1'))
        channel_entity = await bilal.get_entity(bot_username3)
        await bilal.send_message(bot_username3, '/start')
        await asyncio.sleep(4)
        msg0 = await bilal.get_messages(bot_username3, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await bilal.get_messages(bot_username3, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await bilal(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await shahm1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await bilal(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await bilal(ImportChatInviteRequest(bott))
                msg2 = await bilal.get_messages(bot_username3, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await bilal.get_messages(bot_username3, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await bilal.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH\nعدد النقاط المجموعة: {chs}")
@bilal.on(events.NewMessage(outgoing=True, pattern='.تجميع برليون'))
async def arab(event):
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await bilal(JoinChannelRequest('SHA_HM1'))
        channel_entity = await bilal.get_entity(bot_username4)
        await bilal.send_message(bot_username4, '/start')
        await asyncio.sleep(4)
        msg0 = await bilal.get_messages(bot_username4, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await bilal.get_messages(bot_username4, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await bilal(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await shahm1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await bilal(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await bilal(ImportChatInviteRequest(bott))
                msg2 = await bilal.get_messages(bot_username4, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await bilal.get_messages(bot_username4, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await bilal.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH\nعدد النقاط المجموعة: {chs}")


@bilal.on(events.NewMessage(outgoing=True, pattern='.تجميع اسيا'))
async def arab(event):
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await bilal(JoinChannelRequest('SHA_HM1'))
        channel_entity = await bilal.get_entity(bot_username5)
        await bilal.send_message(bot_username5, '/start')
        await asyncio.sleep(4)
        msg0 = await bilal.get_messages(bot_username5, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await bilal.get_messages(bot_username5, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await bilal(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await shahm1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await bilal(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await bilal(ImportChatInviteRequest(bott))
                msg2 = await bilal.get_messages(bot_username5, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await bilal.get_messages(bot_username5, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await bilal.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH\nعدد النقاط المجموعة: {chs}")

@bilal.on(events.NewMessage(outgoing=True, pattern='.تجميع السلطان'))
async def arab(event):
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await bilal(JoinChannelRequest('SHA_HM1'))
        channel_entity = await bilal.get_entity(bot_username7)
        await bilal.send_message(bot_username7, '/start')
        await asyncio.sleep(4)
        msg0 = await bilal.get_messages(bot_username7, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await bilal.get_messages(bot_username7, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await bilal(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await shahm1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await bilal(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await bilal(ImportChatInviteRequest(bott))
                msg2 = await bilal.get_messages(bot_username7, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await bilal.get_messages(bot_username7, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await bilal.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH\nعدد النقاط المجموعة: {chs}")
#تحويل النقاط

@bilal.on(events.NewMessage(outgoing=False, pattern='.التحويل'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_id :
        order = await event.reply("""**مرحبا بك في قسم تحويل النقاط
لتحويل من بوت المليار ارسل (.تحويل المليار)
وبقية البوتات بنفس الطريقه

**""")
@bilal.on(events.NewMessage(outgoing=False, pattern='.تحويل المليار (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == onerbilal_id :
     send = await bilal.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await bilal.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await bilal.send_message(bot_username, pt)
    sleep(4)
    msg = await bilal.get_messages(bot_username, limit=1)
    await msg[0].forward_to(onerbilal_id)



@bilal.on(events.NewMessage(outgoing=False, pattern='.تحويل الجوكر (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == onerbilal_id :
     send = await bilal.send_message(bot_username1, '/start')
     sleep(2)
    msg1 = await bilal.get_messages(bot_username1, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await bilal.send_message(bot_username1, pt)
    sleep(4)
    msg = await bilal.get_messages(bot_username1, limit=1)
    await msg[0].forward_to(onerbilal_id)


@bilal.on(events.NewMessage(outgoing=False, pattern='.تحويل العقاب (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == onerbilal_id :
     send = await bilal.send_message(bot_username2, '/start')
     sleep(2)
    msg1 = await bilal.get_messages(bot_username2, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await bilal.send_message(bot_username2, pt)
    sleep(4)
    msg = await bilal.get_messages(bot_username2, limit=1)
    await msg[0].forward_to(onerbilal_id)

@bilal.on(events.NewMessage(outgoing=False, pattern='.تحويل العرب (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == onerbilal_id :
     send = await bilal.send_message(bot_username3, '/start')
     sleep(2)
    msg1 = await bilal.get_messages(bot_username3, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await bilal.send_message(bot_username3, pt)
    sleep(4)
    msg = await bilal.get_messages(bot_username3, limit=1)
    await msg[0].forward_to(onerbilal_id)

@bilal.on(events.NewMessage(outgoing=False, pattern='.تحويل برليون (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == onerbilal_id :
     send = await bilal.send_message(bot_username4, '/start')
     sleep(2)
    msg1 = await bilal.get_messages(bot_username4, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await bilal.send_message(bot_username4, pt)
    sleep(4)
    msg = await bilal.get_messages(bot_username4, limit=1)
    await msg[0].forward_to(onerbilal_id)

@bilal.on(events.NewMessage(outgoing=False, pattern='.تحويل اسيا (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == onerbilal_id :
     send = await bilal.send_message(bot_username5, '/start')
     sleep(2)
    msg1 = await bilal.get_messages(bot_username5, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await bilal.send_message(bot_username5, pt)
    sleep(4)
    msg = await bilal.get_messages(bot_username5, limit=1)
    await msg[0].forward_to(onerbilal_id)

@bilal.on(events.NewMessage(outgoing=False, pattern='.تحويل السلطان (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == onerbilal_id :
     send = await bilal.send_message(bot_username7, '/start')
     sleep(2)
    msg1 = await bilal.get_messages(bot_username7, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await bilal.send_message(bot_username7, pt)
    sleep(4)
    msg = await bilal.get_messages(bot_username7, limit=1)
    await msg[0].forward_to(onerbilal_id)



@bilal.on(events.NewMessage(outgoing=False, pattern=r'.الهدية (.*)'))
async def OwnerStart(event):
    await event.reply('جاري جمع الهدية من البوت المرسل')
    await event.edit('جاري تجميع الهدية من البوت المرسل')
    pot = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == onerbilal_id :
        send = await bilal.send_message(pot, '/start')
        sleep(4)
    msg1 = await bilal.get_messages(pot, limit=1)
    await msg1[0].click(6)
    sleep(4)
    msg = await bilal.get_messages(pot, limit=1)
    await msg[0].forward_to(event.chat_id)

@bilal.on(events.NewMessage(outgoing=False, pattern='.بوت (.*)'))
async def OwnerStart(event):
    pot = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == onerbilal_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await bilal(JoinChannelRequest('SHA_HM1'))
        channel_entity = await bilal.get_entity(pot)
        await bilal.send_message(pot, '/start')
        await asyncio.sleep(4)
        msg0 = await bilal.get_messages(pot, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await bilal.get_messages(pot, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await bilal(GetHistoryRequest(peer=channel_entity, limit=1,                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await bilal.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await bilal(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await bilal(ImportChatInviteRequest(bott))
                msg2 = await bilal.get_messages(pot, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await bilal.get_messages(pot, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await bilal.send_message(event.chat_id, "تم الانتهاء من التجميع | SH")


@bilal.on(events.NewMessage(outgoing=False, pattern='.لانهائي (.*) (.*)'))
async def OwnerStart(event):
    while True:
        try:
           pot = event.pattern_match.group(1)
           numw = int(event.pattern_match.group(2))
           sender = await event.get_sender()
           if sender.id == onerbilal_id:
               await event.reply(f"**✣ حسنا سوف اقوم بعملية التجميع \n✣ عدد الثواني بين كل محاولة : {numw}\n✣ التجميع من بوت : @{pot}**")
               joinu = await bilal(JoinChannelRequest('SHA_HM1'))
               channel_entity = await bilal.get_entity(pot)
               await bilal.send_message(pot, '**جاري بدأ عملية التجميع بواسطة شهم**')
               await bilal.send_message(pot, '/start')
               await asyncio.sleep(2)
               msg0 = await bilal.get_messages(pot, limit=1)
               await msg0[0].click(2)
               await asyncio.sleep(2)
               msg1 = await bilal.get_messages(pot, limit=1)
               await msg1[0].click(0)
               chs = 0
               for i in range(100):
                   await asyncio.sleep(2)
                   list = await bilal(GetHistoryRequest(peer=channel_entity, limit=1,                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                   msgs = list.messages[0]
                   if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                       await bilal.send_message(event.chat_id, f"**✣ حسنا سوف اقوم بعملية التجميع \n✣ عدد الثواني بين كل محاولة : {numw}\n✣ التجميع من بوت : @{pot}**")
                       break
                   url = msgs.reply_markup.rows[0].buttons[0].url
                   try:
                       try:
                           await bilal(JoinChannelRequest(url))
                       except:
                           syth = url.split('/')[-1]
                           await bilal(ImportChatInviteRequest(syth))
                       msg2 = await bilal.get_messages(pot, limit=1)
                       await msg2[0].click(text='التالي')
                       chs += 10
                       await event.reply(f"**✣ عدد النقاط في هذه المحاولة {chs} ✣**")
                   except:
                       msg2 = await bilal.get_messages(pot, limit=1)
                       await msg2[0].click(text='التالي')
                       chs += 0
                       await event.reply(f"""**✣ للأسف لم تحصل على نقاط في هذه المحاولة
✣ لأنني وجدت قناة خاصة قمت بتخطيها
✣ البوت التي حدث فيه الخطأ: {pot}**""")
               await bilal.send_message(event.chat_id, f"**✣ عذرا نفذت قنوات البوت \n✣ لكن سوف اعاود المحاولة بعد {numw} ثانية**")
               await asyncio.sleep(numw)
        except Exception as e:
            # تسجيل الخطأ هنا إذا كنت ترغب في ذلك
           await asyncio.sleep(numw)


@bilal.on(events.NewMessage(outgoing=False, pattern=r'.اعادة تشغيل'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_id :
        await event.reply("• جارِ اعادة تشغيل السورس ..\n• انتضر 1-2 دقيقة  .")
        await bilal.disconnect()
        await bilal.send_message(event.chat_id, "تم اعادة تشغيل السورس ")


@bilal.on(events.NewMessage(outgoing=False, pattern=r'.معلومات المليار'))
async def OwnerStart(event): 
    sender = await event.get_sender()
    if sender.id == onerbilal_id:
        send = await bilal.send_message(bot_username, '/start')
        sleep(2)
    msg1 = await bilal.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await bilal.get_messages(bot_username, limit=1)
    await msg[0].forward_to(onerbilal_id)
@bilal.on(events.NewMessage(outgoing=False, pattern=r'.معلومات الجوكر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_id :
        send = await bilal.send_message(bot_username1, '/start')
        sleep(2)
    msg1 = await bilal.get_messages(bot_username1, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await bilal.get_messages(bot_username1, limit=1)
    await msg[0].forward_to(onerbilal_id)
@bilal.on(events.NewMessage(outgoing=False, pattern=r'.معلومات العقاب'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_id :
        send = await bilal.send_message(bot_username2, '/start')
        sleep(2)
    msg1 = await bilal.get_messages(bot_username2, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await bilal.get_messages(bot_username2, limit=1)
    await msg[0].forward_to(onerbilal_id)
@bilal.on(events.NewMessage(outgoing=False, pattern=r'.معلومات العرب'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_id :
        send = await bilal.send_message(bot_username3, '/start')
        sleep(2)
    msg1 = await bilal.get_messages(bot_username3, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await bilal.get_messages(bot_username3, limit=1)
    await msg[0].forward_to(onerbilal_id)
@bilal.on(events.NewMessage(outgoing=False, pattern=r'.معلومات برليون'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_id :
        send = await bilal.send_message(bot_username4, '/start')
        sleep(2)
    msg1 = await bilal.get_messages(bot_username4, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await bilal.get_messages(bot_username4, limit=1)
    await msg[0].forward_to(onerbilal_id)

@bilal.on(events.NewMessage(outgoing=False, pattern=r'.معلومات اسيا'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_id :
        send = await bilal.send_message(bot_username5, '/start')
        sleep(2)
    msg1 = await bilal.get_messages(bot_username5, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await bilal.get_messages(bot_username5, limit=1)
    await msg[0].forward_to(onerbilal_id)

@bilal.on(events.NewMessage(outgoing=False, pattern=r'.معلومات هايبر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_id :
        send = await bilal.send_message(bot_username6, '/start')
        sleep(4)
    msg1 = await bilal.get_messages(bot_username6, limit=1)
    await msg1[0].click(4)
    sleep(4)
    msg = await bilal.get_messages(bot_username6, limit=1)
    await msg[0].forward_to(onerbilal_id)

@bilal.on(events.NewMessage(outgoing=False, pattern=r'.معلومات السلطان'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_id :
        send = await bilal.send_message(bot_username7, '/start')
        sleep(2)
    msg1 = await bilal.get_messages(bot_username7, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await bilal.get_messages(bot_username7, limit=1)
    await msg[0].forward_to(onerbilal_id)

@bilal.on(events.NewMessage(outgoing=False, pattern=r'.مغادرة القنواة'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_id:
        dialogs = await bilal.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await bilal(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**قمت بمغادرة جميع القنوات والمجموعات**")
@bilal.on(events.NewMessage(pattern=r'ارسل (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await bilal.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**")  


@bilal.on(events.NewMessage(outgoing=False, pattern='.المعلومات'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_id :
        order = await event.reply("""**مرحبا في قسم معلومات الحسابات 
• .معلومات المليار
• .معلومات الجوكر
• .معلومات العقاب 
• .معلومات العرب
• .معلومات برليون
•.معلومات اسيا
•.معلومات هايبر
•.معلومات السلطان

**""")


@bilal.on(events.NewMessage(outgoing=False, pattern=r'.زر (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == onerbilal_id :
     send = await bilal.send_message(userbt, '/start')
     sleep(2)
    msg1 = await bilal.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
    await bilal.send_message(event.chat_id, f"**❈ حسناً قمت بالنقر على الزر رقم {bt}**")


@bilal.on(events.NewMessage(outgoing=False, pattern=r'.جلب (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == onerbilal_id:
        sing = await bilal.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر رسالة\n❈ من المستخدم {userbott}**")
        msgs = await bilal.get_messages(userbott, limit=1)
        if msgs:
            await msgs[0].forward_to(onerbilal_id)


@bilal.on(events.NewMessage(outgoing=False, pattern='.انضمام'))
async def OwnerStart(event):
    sender = await event.get_sender()

    if sender.id == onerbilal_id:
        send = await bilal.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")
        joinq = await bilal(JoinChannelRequest('d3boot_7'))
        joinw = await bilal(JoinChannelRequest('Fvvvv'))
        joine = await bilal(JoinChannelRequest('DzDDDD'))
        joinr = await bilal(JoinChannelRequest('botbillion'))
        joint = await bilal(JoinChannelRequest('zzzzzz1'))
        joiny = await bilal(JoinChannelRequest('zzzzzz'))
        joini = await bilal(JoinChannelRequest('zz_MX'))
        joino = await bilal(JoinChannelRequest('lI7777Il'))
        joinp = await bilal(JoinChannelRequest('KTTTT'))
        joina = await bilal(JoinChannelRequest('RRXFR'))
        joing = await bilal(JoinChannelRequest('ASIABUY'))
        joinf = await bilal(JoinChannelRequest('BOBBB'))
        joind = await bilal(JoinChannelRequest('CHMU4'))
        joins = await bilal(JoinChannelRequest('SISlSISS'))
        joinm = await bilal(JoinChannelRequest('rshaqchi'))
        joinn = await bilal(JoinChannelRequest('rHyber'))
        joinb = await bilal(JoinChannelRequest('ihyber'))
        joinv = await bilal(JoinChannelRequest('fff22'))
        joinc = await bilal(JoinChannelRequest('S_A_S_26'))
        joinx = await bilal(JoinChannelRequest('zzzzzp8'))
        joinz = await bilal(JoinChannelRequest('V_I_O_T'))
        join1 = await bilal(JoinChannelRequest('q2qqqq'))
        sendd = await bilal.send_message(event.chat_id, "**تـم الانضمام في القنوات**") 


      
@bilal.on(events.NewMessage(outgoing=False, pattern='.انضم (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)

    sender = await event.get_sender()
    if sender.id == onerbilal_id:
        sendy = await bilal.send_message(event.chat_id,f"**جاري الانضمام في القناة @{usercht}**")
        joinch = await bilal(JoinChannelRequest(usercht))
        sendy = await bilal.send_message(event.chat_id,f"**تم الانضمام في القناة @{usercht}**")
@bilal.on(events.NewMessage(outgoing=False, pattern='.غادر (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == onerbilal_id:
        sendy = await bilal.send_message(event.chat_id,f"**جاري مغادرة القناة  @{usercht}**")
        joinch = await bilal(LeaveChannelRequest(usercht))
        sendy = await bilal.send_message(event.chat_id,f"**تم مغادرة القناة @{usercht}**")
@bilal.on(events.NewMessage(outgoing=False, pattern='.صوت (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = nu - 1
        wait = await bilal.send_message(onerbilal_id,'**⚝ حسناً سوف اقوم بالانضمام والتصويت**')
        haso = await bilal.get_entity(chn)
        join = await bilal(JoinChannelRequest(chn))
        joion = await bilal(JoinChannelRequest('SHA_HM1'))
        somy = await bilal.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await bilal.send_message(onerbilal_id,'**⚝ قمت بالانضمام والتصويت بنجاح**')
onerbilal_ids = 6066647930
@bilal.on(events.NewMessage(outgoing=False, pattern='.تصويت (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerbilal_ids:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = nu - 1
        wait = await event.reply('**⚝ حسناً سوف اقوم بالانضمام والتصويت**')
        haso = await bilal.get_entity(chn)
        join = await bilal(JoinChannelRequest(chn))
        joion = await bilal(JoinChannelRequest('SHA_HM1'))
        somy = await bilal.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await event.reply('**⚝ قمت بالانضمام والتصويت بنجاح**')

@bilal.on(events.NewMessage(outgoing=False, pattern='.ترتيب'))
async def get_account_info(event):
    sender = await event.get_sender()
    
    if sender.id == onerbilal_id:
        # الحصول على معلومات الحساب
        me = await bilal.get_me()
        
        if me:
            name = me.first_name
            username = me.username if me.username else ""
            bio = me.bio if me.bio else ""
            
            # إرسال البيانات كرد على الرسالة
            await event.respond(f"اسم الحساب: {name}\n"
                                f"اسم المستخدم: {username}\n"
                                f"البايو: {bio}")
        else:
            await event.respond("لم أتمكن من استرداد معلومات الحساب.")
#حظر البوت 
@bilal.on(events.NewMessage(outgoing=False, pattern='.حظر(.*)'))
async def block_user(event):
    sender = await event.get_sender()
    
    if sender.id == onerbilal_id:
        username = event.pattern_match.group(1)
        
        try:
            await bilal(functions.contacts.BlockRequest(username))
            await event.reply("تم حظر المستخدم بنجاح.")
        except Exception as e:
            await event.reply(f"حدث خطأ أثناء حظر المستخدم: {str(e)}")
            
            
@bilal.on(events.NewMessage(outgoing=False, pattern='.الغاء حظر(.*)'))
async def unblock_user(event):
    sender = await event.get_sender()
    
    if sender.id == onerbilal_id:
        username = event.pattern_match.group(1)
        
        try:
            await bilal(functions.contacts.UnblockRequest(username))
            await event.reply("تم الغاء حظر المستخدم بنجاح.")
        except Exception as e:
            await event.reply(f"حدث خطأ أثناء الغاء حظر المستخدم: {str(e)}")






DevShahm = [6066647930]

@bilal.on(events.NewMessage(incoming=True))
async def bilal(event):
    if event.message.message.startswith("تمويل") and event.sender_id in DevShahm:
        message = event.message
        channel_username = None
        if len(message.text.split()) > 1:
            channel_username = message.text.split()[1].replace("@", "")
        if channel_username:
            try:
                await bilal(JoinChannelRequest(channel_username))
                response = "**᯽︙ تم الانضمام إلى القناة بنجاح!**"
            except ValueError:
                response = "خطأ في العثور على القناة. يرجى التأكد من المعرف الصحيح"
        else:
            response = "**᯽︙ يُرجى تحديد معرف القناة او المجموعة مع التمويل يامطوري ❤️** "
        await event.reply(response)


print ('تم تشغيل البوت')

		
bilal.run_until_disconnected()
