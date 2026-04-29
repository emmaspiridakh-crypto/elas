print(">>> BOT FILE LOADED <<<")

import os, discord, asyncio, json, time, re
from discord.ext import commands
from flask import Flask
from threading import Thread
import datetime

app = Flask('')

@app.route('/')
def home():
    return "OK"

def run():
    app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()

TOKEN = os.getenv("TOKEN")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
GUILD_ID = 1490079978300117212

# ── ROLE IDs ──────────────────────────────────────────────────
FOUNDER_ROLE_ID        = 1490084094749573151
OWNER_ID               = 1490084247682285699
CO_OWNER_ID            = 1490136469287993464
DEVELOPER_ID           = 1490134524221460621
MANAGER_ID             = 1490134503249936525
STAFF_ID               = 1490088402656170045
JOBORG_ID              = 1490338701799194767
APPLICATION_MANAGER_ID = 1490134509830803507
DUTY_ROLE_ID           = 1490338840395649266
AUTOROLE_ID            = 1490134521687969864
DONATE_MANAGER_ID      = 1490134506793861193

WHITELIST_MANAGER_ROLE_ID    = 1490339511186489437
WHITELIST_ROLE_ID            = 1490339131341930577
STAFF_APP_ROLE_ID            = 1490134518768730204
MANAGER_APP_ROLE_ID          = 1490134518768730204
WHITELIST_RESULTS_CHANNEL_ID = 1490340158283972800
WHITELIST_CATEGORY_ID        = 1490340549125865683
STAFF_RESULTS_CHANNEL_ID     = 1490340185576181770
STAFF_CATEGORY_ID            = 1490341195090755844
MANAGER_RESULTS_CHANNEL_ID   = 1490340217687769259
MANAGER_CATEGORY_ID          = 1490341277567549550
DUTY_LOG_CHANNEL_ID          = 1490341619059261510
DUTY_LEADERBOARD_CHANNEL_ID  = 1490341549719162971
SECURITY_LOG_CHANNEL_ID      = 1490340271156756490
SUGGESTION_CHANNEL_ID        = 1491916043709579284
REVIEW_CHANNEL_ID            = 1490702704782217381
INVITE_LOG_CHANNEL_ID        = 1490493231107145820

MAIN_TICKET_CATEGORY_ID   = 1490134558182473959
JOB_TICKET_CATEGORY_ID    = 1490134559315197992
DONATE_TICKET_CATEGORY_ID = 1495232331131125791
TEMP_VOICE_CATEGORY_ID    = 1490134557272313947
TEMP_VOICE_CHANNEL_ID     = 1490134590608642179

BOT_LOG_ID                    = 1490134570056683670
MESSAGE_EDIT_LOG_CHANNEL_ID   = 1490134573986873475
MESSAGE_DELETE_LOG_CHANNEL_ID = 1490134573986873475
MEMBER_JOIN_LOG_CHANNEL_ID    = 1490134577933582387
MEMBER_LEAVE_LOG_CHANNEL_ID   = 1490134577933582387
ROLE_UPDATE_LOG_CHANNEL_ID    = 1491807147133108294
VOICE_LOG_CHANNEL_ID          = 1490134572225134702
CHANNEL_CREATE_LOG_CHANNEL_ID = 1491807225084121321
CHANNEL_DELETE_LOG_CHANNEL_ID = 1491807225084121321
ROLE_CREATE_LOG_CHANNEL_ID    = 1491807147133108294
ROLE_DELETE_LOG_CHANNEL_ID    = 1491807147133108294
TICKET_LOG_ID                 = 1490134569025011784

MEMBERS_CHANNEL_ID = 1490134565145022544
BOTS_CHANNEL_ID    = 1490134568009990154
ONLINE_CHANNEL_ID  = 1490134566558502994
BOOSTS_CHANNEL_ID  = 1490134571147071538

APPLICATION_MANAGER_ROLES = [FOUNDER_ROLE_ID, OWNER_ID, CO_OWNER_ID, WHITELIST_MANAGER_ROLE_ID, APPLICATION_MANAGER_ID]

SERVER_THUMBNAIL_URL = "https://i.imgur.com/F6vMnVL.jpeg"
BANNER_SUPPORT  = "https://i.imgur.com/YL0btaL.jpeg"
BANNER_JOB      = "https://i.imgur.com/YL0btaL.jpeg"
BANNER_APP      = "https://i.imgur.com/YL0btaL.jpeg"
BANNER_SUGGEST  = "https://i.imgur.com/YL0btaL.jpeg"
BANNER_REVIEW   = "https://i.imgur.com/YL0btaL.jpeg"
BANNER_DONATE   = "https://i.imgur.com/YL0btaL.jpeg"

WHITELIST_QUESTIONS = [
    "Ποιο είναι το όνομα στο roblox και η ηλικία σου (IRL);",
    "Δώσε μια σύντομη περιγραφή του χαρακτήρα σου in game.",
    "Ποιο είναι το επάγγελμα που θέλεις να ακολουθήσει ο χαρακτήρας σου;",
    "Τι είναι το Powergaming; Δώσε παράδειγμα.",
    "Τι είναι το Metagaming; Δώσε παράδειγμα.",
    "Πώς αντιδράς όταν κάποιος κάνει RDM/VDM πάνω σου;",
    "Τι είναι το FailRP; Δώσε παράδειγμα.",
    "Τι περιμένεις από την κοινότητα και τι μπορείς να προσφέρεις;"
]
STAFF_QUESTIONS = [
    "Πόσο χρονών είσαι?","Πώς σε λένε στο roblox?","Πόσες ώρες θα μπορείς να είσαι on duty call?",
    "Έχεις εμπειρία απο staff? Αν ναι που?","Τι θα κάνεις αν φίλος σου κάνει abuse perms?",
    "Τι θα κανεις αν ένα member προσβάλει κάποιο staff?","Τι θα κανεις αν υπάρχουν πολλά άτομα στο support?",
    "Τι βήματα θα ακολουθήσεις αν αναφερθεί ένα περιστατικό in game?",
    "Τι θα κάνεις αν αναφερθεί RDM/VDM?","Γιατί να επιλέξουμε εσένα?"
]
MANAGER_QUESTIONS = [
    "Πόσο χρονών είσαι?","Πώς σε λένε στο roblox?","Πόσες ώρες θα μπορείς να είσαι on duty?",
    "Τι θέση manager θέλεις?","Έχεις εμπειρία management? Αν ναι που?",
    "Τι θα κάνεις αν τα μέλη τσακώνονται?","Πως θα κρατήσεις την ομαδικότητα?",
    "Τι θα κάνεις αν ένα member/staff δεν υπακούει τους κανόνες?",
    "Γνωρίζεις ότι σε ticket δεν απαντάς αν έχει ήδη απαντηθεί απο κάποιον?",
    "Τι θα κάνεις αν υπάρχουν πολλά άτομα στο support?","Γιατί να επιλέξουμε εσένα?"
]

# ── PERMISSION HELPERS ────────────────────────────────────────
def is_founder(u):
    return any(r.id == FOUNDER_ROLE_ID for r in u.roles)

def is_owner_or_above(u):
    return any(r.id in (FOUNDER_ROLE_ID, OWNER_ID, CO_OWNER_ID) for r in u.roles)

def is_owner_or_founder(u):
    return any(r.id in (FOUNDER_ROLE_ID, OWNER_ID, CO_OWNER_ID) for r in u.roles)

def is_owner_or_coowner(u):
    return any(r.id in (FOUNDER_ROLE_ID, OWNER_ID, CO_OWNER_ID) for r in u.roles)

def can_manage_applications(u):
    return any(r.id in APPLICATION_MANAGER_ROLES for r in u.roles)

def has_staff_permissions(m):
    return (m.guild_permissions.kick_members or m.guild_permissions.ban_members or
            any(r.id in (STAFF_ID, MANAGER_ID, OWNER_ID, CO_OWNER_ID, FOUNDER_ROLE_ID) for r in m.roles))

def is_staff_or_manager(m):
    return any(r.id in (STAFF_ID, MANAGER_ID, OWNER_ID, CO_OWNER_ID, FOUNDER_ROLE_ID) for r in m.roles)

# ── DATA FILES ────────────────────────────────────────────────
DUTY_FILE = "duty.json"
def load_duty_data():
    if not os.path.exists(DUTY_FILE): open(DUTY_FILE,"w").write("{}")
    return json.load(open(DUTY_FILE))
def save_duty_data(d): json.dump(d, open(DUTY_FILE,"w"), indent=4)
duty_data = load_duty_data()

SECURITY_FILE = "security.json"
def load_security_data():
    if not os.path.exists(SECURITY_FILE):
        json.dump({"spam":{},"ban_kick_tracker":{},"alts":[]}, open(SECURITY_FILE,"w"))
    return json.load(open(SECURITY_FILE))
def save_security_data(d): json.dump(d, open(SECURITY_FILE,"w"), indent=4)
security_data = load_security_data()

ALT_ACCOUNT_AGE_DAYS = 30
ALT_AUTO_KICK        = True
WHITELISTED_BOT_IDS  = set()
URL_PATTERN   = re.compile(r"(https?://|www\.)\S+|discord\.gg/\S+", re.IGNORECASE)
TOKEN_PATTERN = re.compile(r"[MNO][a-zA-Z0-9_-]{23,25}\.[a-zA-Z0-9_-]{6}\.[a-zA-Z0-9_-]{27,38}")

locked_applications = set()

INVITE_FILE = "invites.json"
def load_invite_data():
    if not os.path.exists(INVITE_FILE): open(INVITE_FILE,"w").write("{}")
    return json.load(open(INVITE_FILE))
def save_invite_data(d): json.dump(d, open(INVITE_FILE,"w"), indent=4)
invite_data  = load_invite_data()
invite_cache = {}

# ── SECURITY ALERT ────────────────────────────────────────────
async def send_security_alert(guild, embed, ping=True):
    sec_log = bot.get_channel(SECURITY_LOG_CHANNEL_ID)
    if not sec_log: return
    founder_role = guild.get_role(FOUNDER_ROLE_ID)
    content = founder_role.mention if (ping and founder_role) else None
    asyncio.create_task(sec_log.send(content=content, embed=embed))

# ── VOICE COUNTERS ────────────────────────────────────────────
async def update_voice_channels(guild):
    for ch_id, name in [
        (MEMBERS_CHANNEL_ID, f"👤 Members: {sum(1 for m in guild.members if not m.bot)}"),
        (BOTS_CHANNEL_ID,    f"🤖 Bots: {sum(1 for m in guild.members if m.bot)}"),
        (ONLINE_CHANNEL_ID,  f"🟢 Online: {sum(1 for m in guild.members if m.status != discord.Status.offline)}"),
        (BOOSTS_CHANNEL_ID,  f"🚀 Boosts: {guild.premium_subscription_count}"),
    ]:
        ch = guild.get_channel(ch_id)
        if ch:
            try: await ch.edit(name=name)
            except: pass

@bot.event
async def on_presence_update(before, after): await update_voice_channels(after.guild)
@bot.event
async def on_guild_update(before, after):
    if before.premium_subscription_count != after.premium_subscription_count:
        await update_voice_channels(after)

# ══════════════════════════════════════════════════════════════
#  LOGS
# ══════════════════════════════════════════════════════════════
@bot.event
async def on_voice_state_update(member, before, after):
    guild = member.guild
    log   = bot.get_channel(VOICE_LOG_CHANNEL_ID)

    if after.channel and after.channel.id == TEMP_VOICE_CHANNEL_ID:
        cat = guild.get_channel(TEMP_VOICE_CATEGORY_ID)
        tc  = await guild.create_voice_channel(name=f"{member.name}'s Support", category=cat)
        try: await member.move_to(tc)
        except: pass
        if log:
            e = discord.Embed(title="📞 Support Channel Created", color=discord.Color.blue(), timestamp=discord.utils.utcnow())
            e.set_thumbnail(url=member.display_avatar.url)
            e.add_field(name="👤 Χρήστης", value=f"{member.mention} (`{member.id}`)", inline=True)
            e.add_field(name="📁 Κανάλι",  value=f"**{tc.name}**", inline=True)
            e.set_footer(text=f"Glorious Elas • Voice Log | Channel ID: {tc.id}")
            await log.send(embed=e)

    if (before.channel and before.channel.category_id == TEMP_VOICE_CATEGORY_ID
            and before.channel.id != TEMP_VOICE_CHANNEL_ID
            and len(before.channel.members) == 0):
        try:
            nc = before.channel.name
            await before.channel.delete()
            if log:
                e = discord.Embed(title="🗑️ Support Channel Deleted", color=discord.Color.red(), timestamp=discord.utils.utcnow())
                e.add_field(name="📁 Κανάλι", value=f"**{nc}**", inline=True)
                e.add_field(name="📌 Λόγος",  value="Κανένας μέσα", inline=True)
                e.set_footer(text="Glorious Elas • Voice Log")
                await log.send(embed=e)
        except: pass

    if not log: return

    if not before.channel and after.channel:
        e = discord.Embed(title="🔊 Voice Join", color=discord.Color.green(), timestamp=discord.utils.utcnow())
        e.set_thumbnail(url=member.display_avatar.url)
        e.add_field(name="👤 Χρήστης", value=f"{member.mention} (`{member.id}`)", inline=True)
        e.add_field(name="🔊 Κανάλι",  value=f"**{after.channel.name}**", inline=True)
        e.set_footer(text=f"Glorious Elas • Voice Log | User ID: {member.id}")
        await log.send(embed=e)
    elif before.channel and not after.channel:
        e = discord.Embed(title="🔇 Voice Leave", color=discord.Color.red(), timestamp=discord.utils.utcnow())
        e.set_thumbnail(url=member.display_avatar.url)
        e.add_field(name="👤 Χρήστης", value=f"{member.mention} (`{member.id}`)", inline=True)
        e.add_field(name="🔇 Κανάλι",  value=f"**{before.channel.name}**", inline=True)
        e.set_footer(text=f"Glorious Elas • Voice Log | User ID: {member.id}")
        await log.send(embed=e)
    elif before.channel != after.channel:
        e = discord.Embed(title="🔀 Voice Move", color=discord.Color.yellow(), timestamp=discord.utils.utcnow())
        e.set_thumbnail(url=member.display_avatar.url)
        e.add_field(name="👤 Χρήστης", value=f"{member.mention} (`{member.id}`)", inline=False)
        e.add_field(name="📤 Από",     value=f"**{before.channel.name}**", inline=True)
        e.add_field(name="📥 Σε",      value=f"**{after.channel.name}**",  inline=True)
        e.set_footer(text=f"Glorious Elas • Voice Log | User ID: {member.id}")
        await log.send(embed=e)

@bot.event
async def on_guild_role_create(role):
    log = bot.get_channel(ROLE_CREATE_LOG_CHANNEL_ID)
    if not log: return
    moderator = "Άγνωστος"
    try:
        async for entry in role.guild.audit_logs(limit=1, action=discord.AuditLogAction.role_create):
            moderator = entry.user.mention; break
    except: pass
    e = discord.Embed(title="🆕 Ρόλος Δημιουργήθηκε", color=discord.Color.green(), timestamp=discord.utils.utcnow())
    e.add_field(name="📛 Όνομα",   value=f"**{role.name}**", inline=True)
    e.add_field(name="🎨 Χρώμα",  value=str(role.color),     inline=True)
    e.add_field(name="👤 Από",     value=moderator,           inline=True)
    e.add_field(name="🆔 Role ID", value=f"`{role.id}`",      inline=True)
    e.set_footer(text="Glorious Elas • Role Log")
    await log.send(embed=e)

@bot.event
async def on_guild_role_delete(role):
    log = bot.get_channel(ROLE_DELETE_LOG_CHANNEL_ID)
    if not log: return
    moderator = "Άγνωστος"
    try:
        async for entry in role.guild.audit_logs(limit=1, action=discord.AuditLogAction.role_delete):
            moderator = entry.user.mention; break
    except: pass
    e = discord.Embed(title="🗑️ Ρόλος Διαγράφηκε", color=discord.Color.red(), timestamp=discord.utils.utcnow())
    e.add_field(name="📛 Όνομα",   value=f"**{role.name}**", inline=True)
    e.add_field(name="👤 Από",     value=moderator,           inline=True)
    e.add_field(name="🆔 Role ID", value=f"`{role.id}`",      inline=True)
    e.set_footer(text="Glorious Elas • Role Log")
    await log.send(embed=e)

@bot.event
async def on_member_update(before, after):
    guild = after.guild
    log   = bot.get_channel(ROLE_UPDATE_LOG_CHANNEL_ID)
    if not log: return
    if len(after.roles) > len(before.roles):
        new_role = next(r for r in after.roles if r not in before.roles)
        async for entry in guild.audit_logs(limit=5, action=discord.AuditLogAction.member_role_update):
            if entry.target.id == after.id:
                e = discord.Embed(title="➕ Role Added", color=discord.Color.green(), timestamp=discord.utils.utcnow())
                e.set_thumbnail(url=after.display_avatar.url)
                e.add_field(name="👤 Χρήστης",   value=f"{after.mention} (`{after.id}`)", inline=True)
                e.add_field(name="🎭 Ρόλος",     value=f"**{new_role.name}**",            inline=True)
                e.add_field(name="🛡️ Moderator", value=entry.user.mention,               inline=True)
                e.set_footer(text=f"Glorious Elas • Role Log | Role ID: {new_role.id}")
                await log.send(embed=e); break
    elif len(after.roles) < len(before.roles):
        removed = next(r for r in before.roles if r not in after.roles)
        async for entry in guild.audit_logs(limit=5, action=discord.AuditLogAction.member_role_update):
            if entry.target.id == after.id:
                e = discord.Embed(title="➖ Role Removed", color=discord.Color.red(), timestamp=discord.utils.utcnow())
                e.set_thumbnail(url=after.display_avatar.url)
                e.add_field(name="👤 Χρήστης",   value=f"{after.mention} (`{after.id}`)", inline=True)
                e.add_field(name="🎭 Ρόλος",     value=f"**{removed.name}**",             inline=True)
                e.add_field(name="🛡️ Moderator", value=entry.user.mention,               inline=True)
                e.set_footer(text=f"Glorious Elas • Role Log | Role ID: {removed.id}")
                await log.send(embed=e); break

@bot.event
async def on_guild_channel_create(channel):
    log = bot.get_channel(CHANNEL_CREATE_LOG_CHANNEL_ID)
    if not log: return
    moderator = "Άγνωστος"
    try:
        async for entry in channel.guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_create):
            moderator = entry.user.mention; break
    except: pass
    e = discord.Embed(title="📁 Κανάλι Δημιουργήθηκε", color=discord.Color.green(), timestamp=discord.utils.utcnow())
    e.add_field(name="📛 Όνομα",     value=f"**{channel.name}**",         inline=True)
    e.add_field(name="📂 Τύπος",    value=str(channel.type).capitalize(), inline=True)
    e.add_field(name="👤 Από",       value=moderator,                      inline=True)
    if hasattr(channel, "category") and channel.category:
        e.add_field(name="🗂️ Κατηγορία", value=channel.category.name,   inline=True)
    e.add_field(name="🆔 Channel ID", value=f"`{channel.id}`",            inline=True)
    e.set_footer(text="Glorious Elas • Channel Log")
    await log.send(embed=e)

@bot.event
async def on_guild_channel_delete(channel):
    log = bot.get_channel(CHANNEL_DELETE_LOG_CHANNEL_ID)
    if not log: return
    moderator = "Άγνωστος"
    try:
        async for entry in channel.guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_delete):
            moderator = entry.user.mention; break
    except: pass
    e = discord.Embed(title="🗑️ Κανάλι Διαγράφηκε", color=discord.Color.red(), timestamp=discord.utils.utcnow())
    e.add_field(name="📛 Όνομα",     value=f"**{channel.name}**",         inline=True)
    e.add_field(name="📂 Τύπος",    value=str(channel.type).capitalize(), inline=True)
    e.add_field(name="👤 Από",       value=moderator,                      inline=True)
    e.add_field(name="🆔 Channel ID", value=f"`{channel.id}`",            inline=True)
    e.set_footer(text="Glorious Elas • Channel Log")
    await log.send(embed=e)

@bot.event
async def on_message_edit(before, after):
    if before.author.bot or before.content == after.content: return
    log = bot.get_channel(MESSAGE_EDIT_LOG_CHANNEL_ID)
    if not log: return
    e = discord.Embed(title="✏️ Μήνυμα Επεξεργάστηκε", color=discord.Color.orange(), timestamp=discord.utils.utcnow())
    e.set_thumbnail(url=before.author.display_avatar.url)
    e.add_field(name="👤 Χρήστης", value=f"{before.author.mention} (`{before.author.id}`)", inline=True)
    e.add_field(name="📢 Κανάλι",  value=before.channel.mention, inline=True)
    e.add_field(name="📝 Πριν",    value=before.content[:1020] or "*[κενό]*", inline=False)
    e.add_field(name="📝 Μετά",    value=after.content[:1020]  or "*[κενό]*", inline=False)
    e.add_field(name="🔗 Link",    value=f"[Πήγαινε στο μήνυμα]({after.jump_url})", inline=False)
    e.set_footer(text=f"Glorious Elas • Message Log | User ID: {before.author.id}")
    await log.send(embed=e)

@bot.event
async def on_message_delete(message):
    if message.author.bot: return
    log = bot.get_channel(MESSAGE_DELETE_LOG_CHANNEL_ID)
    if not log: return
    e = discord.Embed(title="🗑️ Μήνυμα Διαγράφηκε", color=discord.Color.red(), timestamp=discord.utils.utcnow())
    e.set_thumbnail(url=message.author.display_avatar.url)
    e.add_field(name="👤 Χρήστης",     value=f"{message.author.mention} (`{message.author.id}`)", inline=True)
    e.add_field(name="📢 Κανάλι",      value=message.channel.mention, inline=True)
    e.add_field(name="📝 Περιεχόμενο", value=message.content[:1020] or "*[χωρίς κείμενο]*", inline=False)
    if message.attachments:
        e.add_field(name="📎 Αρχεία", value="\n".join(a.filename for a in message.attachments), inline=False)
    e.set_footer(text=f"Glorious Elas • Message Log | User ID: {message.author.id}")
    await log.send(embed=e)

# ══════════════════════════════════════════════════════════════
#  TICKET SYSTEM
# ══════════════════════════════════════════════════════════════
class TicketCloseView(discord.ui.View):
    def __init__(self): super().__init__(timeout=None)
    @discord.ui.button(label="🔒 Close Ticket", style=discord.ButtonStyle.red, custom_id="close_ticket_button")
    async def close_ticket(self, interaction, button):
        lc = interaction.guild.get_channel(TICKET_LOG_ID)
        if lc:
            e = discord.Embed(title="❌ Ticket Closed", color=discord.Color.red(), timestamp=discord.utils.utcnow())
            e.set_thumbnail(url=interaction.user.display_avatar.url)
            e.add_field(name="🔒 Έκλεισε από", value=interaction.user.mention, inline=True)
            e.add_field(name="📁 Κανάλι",       value=interaction.channel.mention, inline=True)
            e.set_footer(text="Glorious Elas • Ticket Log")
            await lc.send(embed=e)
        await interaction.response.send_message("Κλείνει σε 4 δευτερόλεπτα...")
        await asyncio.sleep(4)
        try: await interaction.channel.delete()
        except: pass

class MainTicketSelect(discord.ui.Select):
    def __init__(self):
        opts = [
            discord.SelectOption(label="Ανώτατη Διοίκηση", description="Επικοινωνία με Ανώτατη Διοίκηση", emoji="👑"),
            discord.SelectOption(label="Support",           description="Γενική υποστήριξη",               emoji="💬"),
            discord.SelectOption(label="Other",             description="Άλλο αίτημα",                     emoji="📋"),
        ]
        super().__init__(custom_id="main_ticket_select", placeholder="Επίλεξε κατηγορία...", min_values=1, max_values=1, options=opts)

    async def callback(self, interaction):
        guild=interaction.guild; author=interaction.user
        cat=guild.get_channel(MAIN_TICKET_CATEGORY_ID)
        if not cat: return await interaction.response.send_message("Κατηγορία δεν βρέθηκε.", ephemeral=True)
        ow={guild.default_role: discord.PermissionOverwrite(view_channel=False),
            author: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)}
        v=self.values[0]
        if v=="Ανώτατη Διοίκηση":
            rids=[OWNER_ID,CO_OWNER_ID,FOUNDER_ROLE_ID]
            name=f"anotati-{author.name}".replace(" ","-").lower()
            tt="Ανώτατη Διοίκηση"
        elif v=="Support":
            rids=[STAFF_ID,MANAGER_ID,OWNER_ID,CO_OWNER_ID,FOUNDER_ROLE_ID]
            name=f"support-{author.name}".replace(" ","-").lower()
            tt="Support"
        else:
            rids=[STAFF_ID,MANAGER_ID,OWNER_ID,CO_OWNER_ID,FOUNDER_ROLE_ID]
            name=f"other-{author.name}".replace(" ","-").lower()
            tt="Other"
        for rid in rids:
            r=guild.get_role(rid)
            if r: ow[r]=discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)
        ch=await guild.create_text_channel(name=name, category=cat, overwrites=ow)
        e=discord.Embed(title=f"🎫 {tt}",
            description=f"Γεια σου {author.mention}!\n\n**Το staff θα σε εξυπηρετήσει σύντομα.**\nΠαρακαλώ περίγραψε το αίτημά σου.\n\n*One active ticket at a time.*",
            color=discord.Color.from_rgb(20,20,40))
        e.set_image(url=BANNER_SUPPORT); e.set_thumbnail(url=SERVER_THUMBNAIL_URL)
        e.set_footer(text="Glorious Elas • Support System")
        await ch.send(embed=e, view=TicketCloseView())
        lc=guild.get_channel(TICKET_LOG_ID)
        if lc:
            le=discord.Embed(title="📂 Νέο Ticket", color=discord.Color.blue(), timestamp=discord.utils.utcnow())
            le.set_thumbnail(url=author.display_avatar.url)
            le.add_field(name="👤 Από",    value=author.mention, inline=True)
            le.add_field(name="📋 Τύπος", value=tt,             inline=True)
            le.add_field(name="📁 Κανάλι",value=ch.mention,     inline=True)
            le.set_footer(text="Glorious Elas • Ticket Log")
            await lc.send(embed=le)
        await interaction.response.send_message(f"Δημιουργήθηκε: {ch.mention}", ephemeral=True)

class MainTicketPanel(discord.ui.View):
    def __init__(self): super().__init__(timeout=None); self.add_item(MainTicketSelect())

class JobTicketSelect(discord.ui.Select):
    def __init__(self):
        opts=[
            discord.SelectOption(label="Ελληνική Αστυνομία", description="Αίτηση για Ελληνική Αστυνομία", emoji="👮"),
            discord.SelectOption(label="Λιμενικό",            description="Αίτηση για Λιμενικό",           emoji="⚓"),
        ]
        super().__init__(custom_id="job_ticket_select", placeholder="Επίλεξε υπηρεσία...", min_values=1, max_values=1, options=opts)

    async def callback(self, interaction):
        guild=interaction.guild; author=interaction.user
        cat=guild.get_channel(JOB_TICKET_CATEGORY_ID)
        if not cat: return await interaction.response.send_message("Κατηγορία δεν βρέθηκε.", ephemeral=True)
        ow={guild.default_role: discord.PermissionOverwrite(view_channel=False),
            author: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)}
        v=self.values[0]
        if v=="Ελληνική Αστυνομία":
            tt="Ελληνική Αστυνομία"
            name=f"astynomia-{author.name}".replace(" ","-").lower()
        else:
            tt="Λιμενικό"
            name=f"limeniko-{author.name}".replace(" ","-").lower()
        r=guild.get_role(JOBORG_ID)
        if r: ow[r]=discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)
        ch=await guild.create_text_channel(name=name, category=cat, overwrites=ow)
        e=discord.Embed(title=f"🎫 {tt}",
            description=f"Γεια σου {author.mention}!\n\n**Job Manager θα σε εξυπηρετήσει.**\n\n*One active ticket at a time.*",
            color=discord.Color.from_rgb(20,20,40))
        e.set_image(url=BANNER_JOB); e.set_thumbnail(url=SERVER_THUMBNAIL_URL)
        e.set_footer(text="Glorious Elas • Job System")
        await ch.send(embed=e, view=TicketCloseView())
        lc=guild.get_channel(TICKET_LOG_ID)
        if lc:
            le=discord.Embed(title="📂 Νέο Job Ticket", color=discord.Color.blue(), timestamp=discord.utils.utcnow())
            le.set_thumbnail(url=author.display_avatar.url)
            le.add_field(name="👤 Από",    value=author.mention, inline=True)
            le.add_field(name="📋 Τύπος", value=tt,             inline=True)
            le.add_field(name="📁 Κανάλι",value=ch.mention,     inline=True)
            le.set_footer(text="Glorious Elas • Ticket Log")
            await lc.send(embed=le)
        await interaction.response.send_message(f"Δημιουργήθηκε: {ch.mention}", ephemeral=True)

class JobTicketPanel(discord.ui.View):
    def __init__(self): super().__init__(timeout=None); self.add_item(JobTicketSelect())

class DonateTicketSelect(discord.ui.Select):
    def __init__(self):
        opts=[discord.SelectOption(label="Make a Donate", description="Κάνε donate στον server", emoji="💎")]
        super().__init__(custom_id="donate_ticket_select", placeholder="Επίλεξε κατηγορία...", min_values=1, max_values=1, options=opts)

    async def callback(self, interaction):
        guild=interaction.guild; author=interaction.user
        cat=guild.get_channel(DONATE_TICKET_CATEGORY_ID)
        if not cat: return await interaction.response.send_message("Κατηγορία δεν βρέθηκε.", ephemeral=True)
        ow={guild.default_role: discord.PermissionOverwrite(view_channel=False),
            author: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)}
        for rid in [FOUNDER_ROLE_ID, OWNER_ID, DONATE_MANAGER_ID]:
            r=guild.get_role(rid)
            if r: ow[r]=discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)
        name=f"donate-{author.name}".replace(" ","-").lower()
        ch=await guild.create_text_channel(name=name, category=cat, overwrites=ow)
        e=discord.Embed(title="💎 Donate Ticket",
            description=(f"Γεια σου {author.mention}!\n\n"
                         "**Ευχαριστούμε για το ενδιαφέρον σου να κάνεις donate!**\n\n"
                         "Παρακαλώ περίγραψε τι donate θέλεις να κάνεις και ένας από την ομάδα μας θα σε εξυπηρετήσει σύντομα.\n\n"
                         "*One active ticket at a time.*"),
            color=discord.Color.gold())
        e.set_image(url=BANNER_DONATE); e.set_thumbnail(url=SERVER_THUMBNAIL_URL)
        e.set_footer(text="Glorious Elas • Donate System")
        await ch.send(embed=e, view=TicketCloseView())
        lc=guild.get_channel(TICKET_LOG_ID)
        if lc:
            le=discord.Embed(title="💎 Νέο Donate Ticket", color=discord.Color.gold(), timestamp=discord.utils.utcnow())
            le.set_thumbnail(url=author.display_avatar.url)
            le.add_field(name="👤 Από",    value=author.mention, inline=True)
            le.add_field(name="📁 Κανάλι",value=ch.mention,     inline=True)
            le.set_footer(text="Glorious Elas • Ticket Log")
            await lc.send(embed=le)
        await interaction.response.send_message(f"Δημιουργήθηκε: {ch.mention}", ephemeral=True)

class DonateTicketPanel(discord.ui.View):
    def __init__(self): super().__init__(timeout=None); self.add_item(DonateTicketSelect())

# ══════════════════════════════════════════════════════════════
#  APPLICATION SYSTEM
# ══════════════════════════════════════════════════════════════
active_application_sessions = {}

class ReasonModal(discord.ui.Modal):
    def __init__(self, action, target_user_id, app_type, orig_msg):
        super().__init__(title=f"{'Accept' if action=='accept' else 'Deny'} — Reason")
        self.action=action; self.target_user_id=target_user_id; self.app_type=app_type; self.orig_msg=orig_msg
        self.ri=discord.ui.TextInput(label="Reason", style=discord.TextStyle.paragraph, placeholder="Γράψε λόγο...", required=True, max_length=500)
        self.add_item(self.ri)

    async def on_submit(self, interaction):
        guild=interaction.guild; reason=self.ri.value; target=guild.get_member(self.target_user_id)
        at="✅ Accepted" if self.action=="accept" else "❌ Denied"
        color=discord.Color.green() if self.action=="accept" else discord.Color.red()
        if self.orig_msg.embeds:
            oe=self.orig_msg.embeds[0]
            oe.add_field(name=f"{at} by", value=f"{interaction.user.mention} — {reason}", inline=False)
            oe.color=color
            await self.orig_msg.edit(embed=oe, view=None)
        if self.action=="accept":
            rid={"whitelist":WHITELIST_ROLE_ID,"staff":STAFF_APP_ROLE_ID,"manager":MANAGER_APP_ROLE_ID}.get(self.app_type)
            if target and rid:
                r=guild.get_role(rid)
                if r:
                    try: await target.add_roles(r)
                    except: pass
            if target:
                try:
                    dm=discord.Embed(title=f"✅ Αίτηση {self.app_type.capitalize()} έγινε δεκτή!", description=f"**Reason:** {reason}", color=discord.Color.green())
                    await target.send(embed=dm)
                except: pass
        else:
            if target:
                try:
                    dm=discord.Embed(title=f"❌ Αίτηση {self.app_type.capitalize()} απορρίφθηκε.", description=f"**Reason:** {reason}", color=discord.Color.red())
                    await target.send(embed=dm)
                except: pass
                await asyncio.sleep(2)
                try: await target.kick(reason=f"Application denied: {reason}")
                except: pass
        await interaction.response.send_message(f"{at} από {interaction.user.mention}. Reason: {reason}", ephemeral=True)

class ApplicationDecisionView(discord.ui.View):
    def __init__(self, uid, app_type): super().__init__(timeout=None); self.uid=uid; self.app_type=app_type
    @discord.ui.button(label="✅ Accept with Reason", style=discord.ButtonStyle.green, custom_id="app_accept_placeholder")
    async def accept_btn(self, interaction, button):
        if not can_manage_applications(interaction.user): return await interaction.response.send_message("❌ Δεν έχεις δικαίωμα.", ephemeral=True)
        await interaction.response.send_modal(ReasonModal("accept", self.uid, self.app_type, interaction.message))
    @discord.ui.button(label="❌ Deny with Reason", style=discord.ButtonStyle.red, custom_id="app_deny_placeholder")
    async def deny_btn(self, interaction, button):
        if not can_manage_applications(interaction.user): return await interaction.response.send_message("❌ Δεν έχεις δικαίωμα.", ephemeral=True)
        await interaction.response.send_modal(ReasonModal("deny", self.uid, self.app_type, interaction.message))

class StartApplicationView(discord.ui.View):
    def __init__(self, app_type):
        super().__init__(timeout=None); self.app_type=app_type
        lm={"whitelist":"▶️ Start Whitelist","staff":"▶️ Start Staff Application","manager":"▶️ Start Manager Application"}
        self.start_btn.label=lm.get(app_type,"▶️ Start"); self.start_btn.custom_id=f"start_app_{app_type}"
    @discord.ui.button(label="▶️ Start", style=discord.ButtonStyle.blurple, custom_id="start_app_placeholder")
    async def start_btn(self, interaction, button):
        if self.app_type in locked_applications:
            return await interaction.response.send_message(f"🔒 Οι αιτήσεις **{self.app_type.capitalize()}** είναι κλειστές.", ephemeral=True)
        cid=interaction.channel.id
        if cid in active_application_sessions: return await interaction.response.send_message("Αίτηση σε εξέλιξη.", ephemeral=True)
        qs={"whitelist":WHITELIST_QUESTIONS,"staff":STAFF_QUESTIONS,"manager":MANAGER_QUESTIONS}.get(self.app_type,[])
        active_application_sessions[cid]={"user_id":interaction.user.id,"type":self.app_type,"questions":qs,"answers":[],"q_index":0}
        await interaction.response.send_message(f"**Ερώτηση 1/{len(qs)}:**\n{qs[0]}")

class SendApplicationView(discord.ui.View):
    def __init__(self, app_type, uid, qs, ans):
        super().__init__(timeout=None); self.app_type=app_type; self.uid=uid; self.qs=qs; self.ans=ans
    @discord.ui.button(label="📨 Send", style=discord.ButtonStyle.green, custom_id="send_application")
    async def send_btn(self, interaction, button):
        if interaction.user.id!=self.uid: return await interaction.response.send_message("❌ Δεν είσαι εσύ.", ephemeral=True)
        guild=interaction.guild
        rc_id={"whitelist":WHITELIST_RESULTS_CHANNEL_ID,"staff":STAFF_RESULTS_CHANNEL_ID,"manager":MANAGER_RESULTS_CHANNEL_ID}.get(self.app_type)
        rc=guild.get_channel(rc_id); member=guild.get_member(self.uid)
        e=discord.Embed(title=f"📋 Αίτηση {self.app_type.capitalize()} — {member.display_name if member else self.uid}", color=discord.Color.blurple())
        e.set_author(name=str(member), icon_url=member.avatar.url if member and member.avatar else None)
        for q,a in zip(self.qs,self.ans): e.add_field(name=f"❓ {q}", value=f"💬 {a}", inline=False)
        e.set_footer(text=f"User ID: {self.uid}")
        if rc: await rc.send(embed=e, view=ApplicationDecisionView(self.uid, self.app_type))
        await interaction.response.edit_message(content="✅ Η αίτησή σου στάλθηκε!", view=None)
        if interaction.channel.id in active_application_sessions: del active_application_sessions[interaction.channel.id]

async def handle_application_message(message):
    cid=message.channel.id
    if cid not in active_application_sessions: return False
    s=active_application_sessions[cid]
    if message.author.id!=s["user_id"]: return False
    s["answers"].append(message.content); s["q_index"]+=1
    qs=s["questions"]; qi=s["q_index"]
    if qi<len(qs): await message.channel.send(f"**Ερώτηση {qi+1}/{len(qs)}:**\n{qs[qi]}")
    else:
        v=SendApplicationView(s["type"],s["user_id"],qs,s["answers"])
        await message.channel.send("✅ Απάντησες σε όλες! Πάτα **Send** για να στείλεις.", view=v)
    return True

class ApplicationSelect(discord.ui.Select):
    def __init__(self):
        opts=[discord.SelectOption(label="📋 Whitelist",          description="Αίτηση για να παίξεις", emoji="📋", value="whitelist"),
              discord.SelectOption(label="👮 Staff Application",  description="Αίτηση για Staff",      emoji="👮", value="staff"),
              discord.SelectOption(label="👔 Manager Application",description="Αίτηση για Manager",    emoji="👔", value="manager")]
        super().__init__(custom_id="unified_application_select", placeholder="📂 Επίλεξε τύπο αίτησης...", min_values=1, max_values=1, options=opts)

    async def callback(self, interaction):
        app=self.values[0]
        if app in locked_applications:
            return await interaction.response.send_message(f"🔒 Οι αιτήσεις **{app.capitalize()}** είναι κλειστές.", ephemeral=True)
        guild=interaction.guild; author=interaction.user
        cat_id={"whitelist":WHITELIST_CATEGORY_ID,"staff":STAFF_CATEGORY_ID,"manager":MANAGER_CATEGORY_ID}.get(app)
        cat=guild.get_channel(cat_id); cname=f"{app}-{author.name}".replace(" ","-").lower()
        ex=discord.utils.get(guild.text_channels, name=cname)
        if ex: return await interaction.response.send_message(f"Έχεις ήδη: {ex.mention}", ephemeral=True)
        ow={guild.default_role: discord.PermissionOverwrite(view_channel=False),
            author: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)}
        for rid in APPLICATION_MANAGER_ROLES:
            r=guild.get_role(rid)
            if r: ow[r]=discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)
        ch=await guild.create_text_channel(name=cname, category=cat, overwrites=ow)
        tm={"whitelist":"📋 Whitelist Application","staff":"👮 Staff Application","manager":"👔 Manager Application"}
        dm={"whitelist":"Κάνε αίτηση για whitelist.","staff":"Κάνε αίτηση για Staff.","manager":"Κάνε αίτηση για Manager."}
        e=discord.Embed(title=tm.get(app,"Application"), description=f"{author.mention}, {dm.get(app,'')}\n\nΠάτα το κουμπί παρακάτω.", color=discord.Color.blurple())
        e.set_image(url=BANNER_APP); e.set_thumbnail(url=SERVER_THUMBNAIL_URL)
        e.set_footer(text="Glorious Elas • Applications")
        await ch.send(embed=e, view=StartApplicationView(app))
        await interaction.response.send_message(f"Δημιουργήθηκε: {ch.mention}", ephemeral=True)

class UnifiedApplicationPanel(discord.ui.View):
    def __init__(self): super().__init__(timeout=None); self.add_item(ApplicationSelect())

# ══════════════════════════════════════════════════════════════
#  DUTY SYSTEM — persistent leaderboard
# ══════════════════════════════════════════════════════════════
def get_total_seconds(uid: str, now: float) -> float:
    d = duty_data.get(uid, {})
    if not isinstance(d, dict): return 0.0
    total = d.get("total_seconds", 0.0)
    if "start_time" in d:
        total += now - d["start_time"]
    return total

class DutyView(discord.ui.View):
    def __init__(self): super().__init__(timeout=None)

    @discord.ui.button(label="🟢 On Duty", style=discord.ButtonStyle.green, custom_id="duty_on", row=0)
    async def on_duty(self, interaction, button):
        uid=str(interaction.user.id); dr=interaction.guild.get_role(DUTY_ROLE_ID)
        if dr in interaction.user.roles: return await interaction.response.send_message("Είσαι ήδη On Duty!", ephemeral=True)
        if dr:
            try: await interaction.user.add_roles(dr)
            except: pass
        if uid not in duty_data or not isinstance(duty_data[uid], dict):
            duty_data[uid] = {"total_seconds": 0.0}
        duty_data[uid]["start_time"] = time.time()
        save_duty_data(duty_data)
        log=bot.get_channel(DUTY_LOG_CHANNEL_ID)
        if log:
            e=discord.Embed(title="🟢 On Duty", description=f"{interaction.user.mention} μπήκε On Duty.", color=discord.Color.green(), timestamp=discord.utils.utcnow())
            e.set_thumbnail(url=interaction.user.display_avatar.url)
            e.set_footer(text=f"Glorious Elas • Duty Log | User ID: {interaction.user.id}")
            await log.send(embed=e)
        await interaction.response.send_message("✅ Είσαι On Duty!", ephemeral=True)

    @discord.ui.button(label="🔴 Off Duty", style=discord.ButtonStyle.red, custom_id="duty_off", row=0)
    async def off_duty(self, interaction, button):
        uid=str(interaction.user.id); dr=interaction.guild.get_role(DUTY_ROLE_ID)
        if dr not in interaction.user.roles: return await interaction.response.send_message("Δεν είσαι On Duty!", ephemeral=True)
        if dr:
            try: await interaction.user.remove_roles(dr)
            except: pass
        ss=0.0
        if uid in duty_data and isinstance(duty_data[uid], dict) and "start_time" in duty_data[uid]:
            ss = time.time() - duty_data[uid]["start_time"]
            duty_data[uid]["total_seconds"] = duty_data[uid].get("total_seconds", 0.0) + ss
            duty_data[uid].pop("start_time", None)
            save_duty_data(duty_data)
        h,r=divmod(int(ss),3600); m,s2=divmod(r,60); ds=f"{h}ω {m}λ {s2}δ"
        total = duty_data.get(uid,{}).get("total_seconds",0.0)
        th,tr=divmod(int(total),3600); tm2,_=divmod(tr,60)
        log=bot.get_channel(DUTY_LOG_CHANNEL_ID)
        if log:
            e=discord.Embed(title="🔴 Off Duty", description=f"{interaction.user.mention} βγήκε Off Duty.", color=discord.Color.red(), timestamp=discord.utils.utcnow())
            e.set_thumbnail(url=interaction.user.display_avatar.url)
            e.add_field(name="⏱ Session",  value=ds,                     inline=True)
            e.add_field(name="📊 Σύνολο",  value=f"{th}ω {tm2}λ",        inline=True)
            e.set_footer(text=f"Glorious Elas • Duty Log | User ID: {interaction.user.id}")
            await log.send(embed=e)
        await interaction.response.send_message(f"✅ Off Duty! Session: **{ds}** | Σύνολο: **{th}ω {tm2}λ**", ephemeral=True)

    @discord.ui.button(label="📋 Duty Status", style=discord.ButtonStyle.blurple, custom_id="duty_status", row=1)
    async def duty_status(self, interaction, button):
        guild=interaction.guild; dr=guild.get_role(DUTY_ROLE_ID); now=time.time()
        on_duty_members=[]
        if dr:
            for m in guild.members:
                if dr in m.roles and not m.bot:
                    uid=str(m.id)
                    if uid in duty_data and "start_time" in duty_data[uid]:
                        elapsed=now-duty_data[uid]["start_time"]
                        h,rem=divmod(int(elapsed),3600); mn,sc=divmod(rem,60)
                        on_duty_members.append((m,f"{h}ω {mn}λ {sc}δ"))
                    else:
                        on_duty_members.append((m,"0ω 0λ 0δ"))
        e=discord.Embed(title="📋 Duty Status", color=discord.Color.blurple(), timestamp=discord.utils.utcnow())
        if on_duty_members:
            e.description="\n".join(f"🟢 {m.mention} — `{dur}`" for m,dur in on_duty_members)
            e.set_footer(text=f"{len(on_duty_members)} άτομα on duty | Glorious Elas")
        else:
            e.description="❌ Κανένας δεν είναι On Duty αυτή τη στιγμή."
            e.set_footer(text="Glorious Elas • Duty Status")
        await interaction.response.send_message(embed=e, ephemeral=True)

    @discord.ui.button(label="🏆 Leaderboard", style=discord.ButtonStyle.grey, custom_id="duty_leaderboard_btn", row=1)
    async def leaderboard_btn(self, interaction, button):
        guild=interaction.guild; now=time.time()
        totals=[]
        for uid,d in duty_data.items():
            if not isinstance(d,dict): continue
            total=get_total_seconds(uid, now)
            if total > 0:
                totals.append((uid,total))
        totals.sort(key=lambda x:x[1], reverse=True)
        medals=["🥇","🥈","🥉"]
        e=discord.Embed(title="🏆 Duty Leaderboard", color=discord.Color.gold(), timestamp=discord.utils.utcnow())
        desc=""
        for i,(uid,secs) in enumerate(totals[:10]):
            member=guild.get_member(int(uid)); name=member.display_name if member else f"User {uid}"
            h,rem=divmod(int(secs),3600); mn,_=divmod(rem,60)
            medal=medals[i] if i<3 else f"**#{i+1}**"
            dr=guild.get_role(DUTY_ROLE_ID)
            is_on=" 🟢" if (member and dr and dr in member.roles) else ""
            desc+=f"{medal} {name}{is_on} — `{h}ω {mn}λ`\n"
        e.description=desc or "Κανένας δεν έχει κάνει duty ακόμα."
        e.set_footer(text="🟢 = Τώρα on duty • Οι χρόνοι δεν επαναφέρονται ποτέ | Glorious Elas")
        await interaction.response.send_message(embed=e, ephemeral=True)

# ══════════════════════════════════════════════════════════════
#  SECURITY SYSTEM
# ══════════════════════════════════════════════════════════════
spam_tracker={}; pending_bots={}; ban_kick_tracker={}

class BotVerificationView(discord.ui.View):
    def __init__(self, bot_member):
        super().__init__(timeout=None); self.bot_member=bot_member
        self.accept_btn.custom_id=f"bot_accept_{bot_member.id}"; self.deny_btn.custom_id=f"bot_deny_{bot_member.id}"

    @discord.ui.button(label="✅ Accept Bot", style=discord.ButtonStyle.green, custom_id="bot_accept_placeholder")
    async def accept_btn(self, interaction, button):
        if not interaction.user.guild_permissions.administrator: return await interaction.response.send_message("❌ Μόνο admins.", ephemeral=True)
        pending_bots.pop(str(self.bot_member.id), None)
        try:
            for ch in interaction.guild.channels:
                try: await ch.set_permissions(self.bot_member, overwrite=None, reason="Bot accepted")
                except: pass
        except: pass
        e=discord.Embed(title="✅ Bot Accepted", description=f"**{self.bot_member}** έγινε accepted από {interaction.user.mention}.", color=discord.Color.green(), timestamp=discord.utils.utcnow())
        await interaction.message.edit(embed=e, view=None); await interaction.response.send_message("✅ Accepted!", ephemeral=True)

    @discord.ui.button(label="❌ Deny Bot (Kick)", style=discord.ButtonStyle.red, custom_id="bot_deny_placeholder")
    async def deny_btn(self, interaction, button):
        if not interaction.user.guild_permissions.administrator: return await interaction.response.send_message("❌ Μόνο admins.", ephemeral=True)
        kicked=False
        try: await self.bot_member.kick(reason=f"Bot denied by {interaction.user}"); kicked=True
        except: pass
        pending_bots.pop(str(self.bot_member.id), None)
        e=discord.Embed(title="❌ Bot Denied & Kicked", description=f"**{self.bot_member}** kicked από {interaction.user.mention}.\nKick: {'✅' if kicked else '❌'}", color=discord.Color.red(), timestamp=discord.utils.utcnow())
        await interaction.message.edit(embed=e, view=None); await interaction.response.send_message("❌ Denied and kicked.", ephemeral=True)

@bot.event
async def on_member_ban(guild, user): await _track_mass_action(guild, user, "ban")

@bot.event
async def on_member_remove(member):
    await asyncio.sleep(1)
    async for entry in member.guild.audit_logs(limit=3, action=discord.AuditLogAction.kick):
        if entry.target.id==member.id and (datetime.datetime.utcnow()-entry.created_at.replace(tzinfo=None)).seconds<5:
            await _track_mass_action(member.guild, entry.user, "kick"); break
    uid=str(member.id)
    if uid in invite_data and "invited_by" in invite_data[uid]:
        iid=invite_data[uid]["invited_by"]
        if iid in invite_data:
            invite_data[iid]["left"]=invite_data[iid].get("left",0)+1
            invite_data[iid]["real"]=max(0,invite_data[iid].get("total",0)-invite_data[iid].get("left",0))
            save_invite_data(invite_data)
    await update_voice_channels(member.guild)
    log=bot.get_channel(MEMBER_LEAVE_LOG_CHANNEL_ID)
    if log:
        roles=[r.mention for r in member.roles if r.name!="@everyone"]
        e=discord.Embed(title="🔴 Μέλος Έφυγε", color=discord.Color.red(), timestamp=discord.utils.utcnow())
        e.set_thumbnail(url=member.display_avatar.url)
        e.add_field(name="👤 Χρήστης",   value=f"{member.mention} (`{member.id}`)", inline=True)
        e.add_field(name="📛 Username",   value=str(member), inline=True)
        e.add_field(name="👥 Μέλη τώρα", value=str(member.guild.member_count), inline=True)
        e.add_field(name="🎭 Ρόλοι",     value=" ".join(roles) if roles else "Κανένας", inline=False)
        e.set_footer(text=f"Glorious Elas • Member Log | User ID: {member.id}")
        await log.send(embed=e)

async def _track_mass_action(guild, moderator, action_type):
    uid=str(moderator.id) if hasattr(moderator,"id") else str(moderator); now=time.time()
    if uid not in ban_kick_tracker: ban_kick_tracker[uid]=[]
    ban_kick_tracker[uid].append(now); ban_kick_tracker[uid]=[t for t in ban_kick_tracker[uid] if now-t<10]
    if len(ban_kick_tracker[uid])>=3:
        ban_kick_tracker[uid]=[]; mm=guild.get_member(int(uid))
        exempt=[FOUNDER_ROLE_ID,OWNER_ID]; is_ex=mm and any(r.id in exempt for r in mm.roles)
        if mm and not is_ex:
            try: await mm.timeout(datetime.timedelta(weeks=1), reason=f"Mass {action_type}")
            except: pass
            e=discord.Embed(title=f"⚠️ Mass {action_type.upper()} Detected!", description=f"{mm.mention} έκανε mass {action_type}.\n**1 εβδομάδα timeout** δόθηκε.", color=discord.Color.dark_red(), timestamp=discord.utils.utcnow())
            await send_security_alert(guild, e, ping=True)

# ══════════════════════════════════════════════════════════════
#  SUGGESTION & REVIEW
# ══════════════════════════════════════════════════════════════
class SuggestionModal(discord.ui.Modal, title="💡 Make a Suggestion"):
    suggestion_input=discord.ui.TextInput(label="Η πρότασή σου", style=discord.TextStyle.paragraph, placeholder="Γράψε εδώ...", required=True, max_length=1000)
    async def on_submit(self, interaction):
        ch=interaction.guild.get_channel(SUGGESTION_CHANNEL_ID)
        if not ch: return await interaction.response.send_message("❌ Κανάλι δεν βρέθηκε.", ephemeral=True)
        e=discord.Embed(title="💡 Νέα Πρόταση", description=self.suggestion_input.value, color=discord.Color.from_rgb(88,101,242), timestamp=discord.utils.utcnow())
        e.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url if interaction.user.avatar else None)
        e.set_thumbnail(url=SERVER_THUMBNAIL_URL); e.set_footer(text=f"User ID: {interaction.user.id} • Glorious Elas")
        msg=await ch.send(embed=e); await msg.add_reaction("👍"); await msg.add_reaction("👎")
        await interaction.response.send_message("✅ Στάλθηκε!", ephemeral=True)

class SuggestionPanelView(discord.ui.View):
    def __init__(self): super().__init__(timeout=None)
    @discord.ui.button(label="💡 Make a Suggestion", style=discord.ButtonStyle.blurple, custom_id="make_suggestion_btn")
    async def make_suggestion(self, interaction, button): await interaction.response.send_modal(SuggestionModal())

class ReviewModal(discord.ui.Modal, title="⭐ Make a Review"):
    review_input=discord.ui.TextInput(label="Το review σου", style=discord.TextStyle.paragraph, placeholder="Γράψε εδώ...", required=True, max_length=1000)
    def __init__(self, stars): super().__init__(); self.stars=stars
    async def on_submit(self, interaction):
        ch=interaction.guild.get_channel(REVIEW_CHANNEL_ID)
        if not ch: return await interaction.response.send_message("❌ Κανάλι δεν βρέθηκε.", ephemeral=True)
        sd="⭐"*self.stars+"☆"*(5-self.stars)
        cm={1:discord.Color.red(),2:discord.Color.orange(),3:discord.Color.yellow(),4:discord.Color.green(),5:discord.Color.from_rgb(255,215,0)}
        e=discord.Embed(title="⭐ Νέο Review", color=cm.get(self.stars,discord.Color.blurple()), timestamp=discord.utils.utcnow())
        e.add_field(name="Αξιολόγηση", value=sd, inline=False)
        e.add_field(name="Σχόλιο", value=self.review_input.value, inline=False)
        e.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url if interaction.user.avatar else None)
        e.set_thumbnail(url=SERVER_THUMBNAIL_URL); e.set_footer(text=f"User ID: {interaction.user.id} • Glorious Elas")
        await ch.send(embed=e); await interaction.response.send_message(f"✅ Review ({sd}) στάλθηκε!", ephemeral=True)

class StarSelect(discord.ui.Select):
    def __init__(self):
        opts=[discord.SelectOption(label="⭐ 1 Αστέρι",         emoji="⭐", value="1"),
              discord.SelectOption(label="⭐⭐ 2 Αστέρια",      emoji="⭐", value="2"),
              discord.SelectOption(label="⭐⭐⭐ 3 Αστέρια",    emoji="⭐", value="3"),
              discord.SelectOption(label="⭐⭐⭐⭐ 4 Αστέρια",  emoji="⭐", value="4"),
              discord.SelectOption(label="⭐⭐⭐⭐⭐ 5 Αστέρια", emoji="⭐", value="5")]
        super().__init__(custom_id="star_select_review", placeholder="⭐ Επίλεξε αξιολόγηση...", min_values=1, max_values=1, options=opts)
    async def callback(self, interaction): await interaction.response.send_modal(ReviewModal(int(self.values[0])))

class StarSelectView(discord.ui.View):
    def __init__(self): super().__init__(timeout=None); self.add_item(StarSelect())

class ReviewPanelView(discord.ui.View):
    def __init__(self): super().__init__(timeout=None)
    @discord.ui.button(label="⭐ Make a Review", style=discord.ButtonStyle.blurple, custom_id="make_review_btn")
    async def make_review(self, interaction, button):
        e=discord.Embed(title="⭐ Επίλεξε Αξιολόγηση", description="Επίλεξε αστέρια και γράψε σχόλιο!", color=discord.Color.from_rgb(255,215,0))
        await interaction.response.send_message(embed=e, view=StarSelectView(), ephemeral=True)

# ══════════════════════════════════════════════════════════════
#  ON MESSAGE
# ══════════════════════════════════════════════════════════════
@bot.event
async def on_message(message):
    if message.author.bot: await bot.process_commands(message); return
    guild=message.guild; author=message.author

    if guild and TOKEN_PATTERN.search(message.content):
        try: await message.delete()
        except: pass
        e=discord.Embed(title="🔑 TOKEN DETECTED & DELETED!", description=f"{author.mention} έστειλε κάτι που μοιάζει με **Bot Token**!\nΤο μήνυμα διαγράφηκε.\n\n⚠️ **Αν είναι δικό σου token, άλλαξέ το ΑΜΕΣΩΣ!**", color=discord.Color.dark_red(), timestamp=discord.utils.utcnow())
        e.set_thumbnail(url=author.display_avatar.url)
        e.add_field(name="👤 Χρήστης", value=f"{author.mention} (`{author.id}`)", inline=True)
        e.add_field(name="📢 Κανάλι",  value=message.channel.mention, inline=True)
        e.set_footer(text="Glorious Elas • Security Log")
        await send_security_alert(guild, e, ping=True); return

    if guild and URL_PATTERN.search(message.content):
        exempt=[FOUNDER_ROLE_ID,OWNER_ID]; is_ex=any(r.id in exempt for r in author.roles)
        if not is_ex and not author.guild_permissions.administrator:
            try: await message.delete()
            except: pass
            try: await author.timeout(datetime.timedelta(hours=1), reason="Link detected")
            except: pass
            e=discord.Embed(title="🔗 Link Detected & Deleted", description=f"{author.mention} έστειλε link και πήρε **1 ώρα timeout**.", color=discord.Color.orange(), timestamp=discord.utils.utcnow())
            e.set_thumbnail(url=author.display_avatar.url)
            e.add_field(name="👤 Χρήστης", value=f"{author.mention} (`{author.id}`)", inline=True)
            e.add_field(name="📢 Κανάλι",  value=message.channel.mention, inline=True)
            e.set_footer(text="Glorious Elas • Security Log")
            await send_security_alert(guild, e, ping=False); return

    if guild:
        uid=str(author.id); now=time.time()
        if uid not in spam_tracker: spam_tracker[uid]=[]
        spam_tracker[uid].append(now); spam_tracker[uid]=[t for t in spam_tracker[uid] if now-t<5]
        if len(spam_tracker[uid])>=5:
            spam_tracker[uid]=[]
            if not author.guild_permissions.administrator:
                try: await author.timeout(datetime.timedelta(minutes=10), reason="Spam")
                except: pass
                e=discord.Embed(title="🚫 Spam Detected", description=f"{author.mention} έκανε spam και πήρε **10 λεπτά timeout**.", color=discord.Color.red(), timestamp=discord.utils.utcnow())
                e.set_thumbnail(url=author.display_avatar.url)
                e.add_field(name="👤 Χρήστης", value=f"{author.mention} (`{author.id}`)", inline=True)
                e.add_field(name="📢 Κανάλι",  value=message.channel.mention, inline=True)
                e.set_footer(text="Glorious Elas • Security Log")
                await send_security_alert(guild, e, ping=False)

    handled=await handle_application_message(message)
    if not handled: await bot.process_commands(message)

# ══════════════════════════════════════════════════════════════
#  ON MEMBER JOIN
# ══════════════════════════════════════════════════════════════
@bot.event
async def on_member_join(member):
    guild=member.guild

    if member.bot:
        if member.id in WHITELISTED_BOT_IDS: return
        try:
            for ch in guild.channels:
                try: await ch.set_permissions(member, send_messages=False, read_messages=False, connect=False, speak=False, reason="Bot pending verification")
                except: pass
        except: pass
        is_v=bool(member.public_flags and discord.PublicUserFlags.verified_bot in member.public_flags)
        bt="✅ Verified Bot" if is_v else "⚠️ Unverified / Custom / Fake Bot"
        color=discord.Color.yellow() if is_v else discord.Color.dark_red()
        e=discord.Embed(title=f"🤖 Νέο Bot! {'(UNVERIFIED ⚠️)' if not is_v else '(Verified)'}",
            description=f"**{member}** ({member.mention}) μπήκε.\n\n**Τύπος:** {bt}\n**ID:** `{member.id}`\n**Δημιουργήθηκε:** <t:{int(member.created_at.timestamp())}:F>\n\n⚠️ Μηδενικά permissions μέχρι Accept.",
            color=color, timestamp=discord.utils.utcnow())
        e.set_thumbnail(url=member.display_avatar.url)
        e.set_footer(text="Glorious Elas • Security Log")
        sl=bot.get_channel(SECURITY_LOG_CHANNEL_ID)
        if sl:
            or_=guild.get_role(OWNER_ID); c=or_.mention if or_ else None
            msg=await sl.send(content=c, embed=e, view=BotVerificationView(member))
            pending_bots[str(member.id)]=msg.id
        return

    age=(datetime.datetime.utcnow()-member.created_at.replace(tzinfo=None)).days
    if age<ALT_ACCOUNT_AGE_DAYS:
        e=discord.Embed(title="🚨 ALT ACCOUNT DETECTED!", color=discord.Color.dark_red(), timestamp=discord.utils.utcnow())
        e.set_thumbnail(url=member.display_avatar.url)
        e.add_field(name="👤 Χρήστης",       value=f"{member.mention} (`{member.id}`)", inline=False)
        e.add_field(name="📅 Ηλικία",        value=f"**{age} ημέρες**", inline=True)
        e.add_field(name="📆 Δημιουργήθηκε", value=f"<t:{int(member.created_at.timestamp())}:F>", inline=True)
        if ALT_AUTO_KICK:
            try:
                await member.kick(reason=f"Alt account — ηλικία: {age} ημέρες")
                e.add_field(name="⚡ Ενέργεια", value="✅ **Auto-kicked**", inline=False)
            except Exception as err:
                e.add_field(name="⚡ Ενέργεια", value=f"❌ Απέτυχε: {err}", inline=False)
        else:
            e.add_field(name="⚡ Ενέργεια", value="⚠️ Μόνο ειδοποίηση", inline=False)
        e.set_footer(text="Glorious Elas • Security Log")
        await send_security_alert(guild, e, ping=True)
        if ALT_AUTO_KICK: return

    r=guild.get_role(AUTOROLE_ID)
    if r:
        try: await member.add_roles(r)
        except: pass

    try:
        ni=await guild.invites(); nim={i.code:i.uses for i in ni}; inviter=None
        for code,ou in invite_cache.get(guild.id,{}).items():
            if nim.get(code,0)>ou:
                for i in ni:
                    if i.code==code: inviter=i.inviter; break
                break
        invite_cache[guild.id]=nim
        if inviter:
            iid=str(inviter.id); mid=str(member.id)
            if mid not in invite_data: invite_data[mid]={}
            invite_data[mid]["invited_by"]=iid
            if iid not in invite_data: invite_data[iid]={"total":0,"real":0,"left":0}
            invite_data[iid]["total"]=invite_data[iid].get("total",0)+1
            invite_data[iid]["real"]=invite_data[iid].get("total",0)-invite_data[iid].get("left",0)
            save_invite_data(invite_data)
            il=bot.get_channel(INVITE_LOG_CHANNEL_ID)
            if il:
                e=discord.Embed(title="📨 Νέο Invite", description=f"{member.mention} μπήκε με invite του {inviter.mention}", color=discord.Color.green(), timestamp=discord.utils.utcnow())
                e.set_thumbnail(url=member.display_avatar.url)
                e.add_field(name="📊 Inviter Stats",
                    value=(f"**Όνομα:** {inviter.display_name}\n"
                           f"**Συνολικά:** {invite_data[iid].get('total',0)}\n"
                           f"**Real:** {invite_data[iid].get('real',0)}\n"
                           f"**Έφυγαν:** {invite_data[iid].get('left',0)}"), inline=False)
                e.set_footer(text=f"Glorious Elas • Invite Log | User ID: {member.id}")
                await il.send(embed=e)
    except Exception as ex: print(f"Invite error: {ex}")

    log=bot.get_channel(MEMBER_JOIN_LOG_CHANNEL_ID)
    if log:
        e=discord.Embed(title="🟢 Μέλος Μπήκε", color=discord.Color.green(), timestamp=discord.utils.utcnow())
        e.set_thumbnail(url=member.display_avatar.url)
        e.add_field(name="👤 Χρήστης",     value=f"{member.mention} (`{member.id}`)", inline=True)
        e.add_field(name="📛 Username",     value=str(member), inline=True)
        e.add_field(name="📅 Λογαριασμός", value=f"<t:{int(member.created_at.timestamp())}:R>", inline=True)
        e.add_field(name="👥 Μέλη τώρα",   value=str(guild.member_count), inline=True)
        e.set_footer(text=f"Glorious Elas • Member Log | User ID: {member.id}")
        await log.send(embed=e)
    await update_voice_channels(guild)

# ══════════════════════════════════════════════════════════════
#  COMMANDS
# ══════════════════════════════════════════════════════════════

# ── MODERATION ────────────────────────────────────────────────
@bot.command()
async def ban(ctx, member: discord.Member=None, *, reason="No reason"):
    if not has_staff_permissions(ctx.author): return await ctx.reply("❌ Δεν έχεις δικαίωμα.")
    if not member: return await ctx.reply("Χρήση: `!ban @user [λόγος]`")
    await member.ban(reason=reason); await ctx.reply(f"🔨 **{member}** banned.")
    log=bot.get_channel(BOT_LOG_ID)
    if log: await log.send(f"🔨 **{ctx.author}** banned **{member}** — {reason}")

@bot.command()
async def kick(ctx, member: discord.Member=None, *, reason="No reason"):
    if not has_staff_permissions(ctx.author): return await ctx.reply("❌ Δεν έχεις δικαίωμα.")
    if not member: return await ctx.reply("Χρήση: `!kick @user [λόγος]`")
    await member.kick(reason=reason); await ctx.reply(f"👢 **{member}** kicked.")
    log=bot.get_channel(BOT_LOG_ID)
    if log: await log.send(f"👢 **{ctx.author}** kicked **{member}** — {reason}")

@bot.command()
async def timeout(ctx, member: discord.Member=None, minutes: int=None, *, reason="No reason"):
    if not has_staff_permissions(ctx.author): return await ctx.reply("❌ Δεν έχεις δικαίωμα.")
    if not member or not minutes: return await ctx.reply("Χρήση: `!timeout @user <minutes> [λόγος]`")
    await member.timeout(datetime.timedelta(minutes=minutes), reason=reason)
    await ctx.reply(f"⏳ **{member}** timeout {minutes} λεπτά.")
    log=bot.get_channel(BOT_LOG_ID)
    if log: await log.send(f"⏳ **{ctx.author}** timed out **{member}** {minutes}min — {reason}")

@bot.command()
async def clearmessage(ctx, amount: int=None):
    if not has_staff_permissions(ctx.author): return await ctx.reply("❌ Δεν έχεις δικαίωμα.")
    if not amount: return await ctx.reply("Χρήση: `!clearmessage <amount>`")
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f"🧹 Διαγράφηκαν **{amount}** μηνύματα.", delete_after=3)

# ── INFO ──────────────────────────────────────────────────────
@bot.command()
async def serverstatus(ctx):
    if not is_staff_or_manager(ctx.author): return await ctx.reply("❌ Δεν έχεις δικαίωμα.")
    g=ctx.guild
    e=discord.Embed(title="📊 Server Status", color=discord.Color.blurple(), timestamp=discord.utils.utcnow())
    e.set_thumbnail(url=g.icon.url if g.icon else None)
    e.add_field(name="👤 Members", value=sum(1 for m in g.members if not m.bot))
    e.add_field(name="🤖 Bots",    value=sum(1 for m in g.members if m.bot))
    e.add_field(name="🟢 Online",  value=sum(1 for m in g.members if m.status!=discord.Status.offline))
    e.add_field(name="🚀 Boosts",  value=g.premium_subscription_count)
    e.set_footer(text="Glorious Elas • Server Status")
    await ctx.reply(embed=e)

@bot.command()
async def invites(ctx, member: discord.Member=None):
    if not is_staff_or_manager(ctx.author): return await ctx.reply("❌ Δεν έχεις δικαίωμα.")
    t=member or ctx.author; uid=str(t.id); d=invite_data.get(uid,{"total":0,"real":0,"left":0})
    e=discord.Embed(title=f"📨 Invites — {t.display_name}", color=discord.Color.blurple(), timestamp=discord.utils.utcnow())
    e.set_thumbnail(url=t.display_avatar.url)
    e.add_field(name="📊 Συνολικά", value=str(d.get("total",0)), inline=True)
    e.add_field(name="✅ Real",     value=str(d.get("real",0)),  inline=True)
    e.add_field(name="🚪 Έφυγαν",  value=str(d.get("left",0)),  inline=True)
    e.set_footer(text="Glorious Elas • Invite Log")
    await ctx.reply(embed=e)

@bot.command()
async def serverinvites(ctx):
    if not is_staff_or_manager(ctx.author): return await ctx.reply("❌ Δεν έχεις δικαίωμα.")
    guild=ctx.guild
    entries=[]
    for uid,d in invite_data.items():
        if not isinstance(d,dict): continue
        total=d.get("total",0)
        if total<=0: continue
        member=guild.get_member(int(uid))
        name=member.display_name if member else f"User {uid}"
        entries.append((name,total,d.get("real",0),d.get("left",0)))
    entries.sort(key=lambda x:x[1], reverse=True)
    e=discord.Embed(title=f"📨 Server Invites — {guild.name}", color=discord.Color.blurple(), timestamp=discord.utils.utcnow())
    if guild.icon: e.set_thumbnail(url=guild.icon.url)
    e.set_image(url=BANNER_SUPPORT)
    if entries:
        medals=["🥇","🥈","🥉"]
        desc=""
        for i,(name,total,real,left) in enumerate(entries[:20]):
            medal=medals[i] if i<3 else f"**#{i+1}**"
            desc+=f"{medal} **{name}** — `{total}` συνολικά | `{real}` real | `{left}` έφυγαν\n"
        e.description=desc
    else:
        e.description="Δεν υπάρχουν δεδομένα invites ακόμα."
    e.set_footer(text=f"Glorious Elas • {guild.member_count} μέλη συνολικά")
    await ctx.send(embed=e)

@bot.command()
async def scan(ctx, member: discord.Member=None):
    if not is_staff_or_manager(ctx.author): return await ctx.reply("❌ Δεν έχεις δικαίωμα.")
    await ctx.reply("🔍 Σκανάρω...", delete_after=2); guild=ctx.guild
    if member:
        age=(datetime.datetime.utcnow()-member.created_at.replace(tzinfo=None)).days
        al=[]; alb={discord.AuditLogAction.ban:"🔨 Ban",discord.AuditLogAction.kick:"👢 Kick",
                    discord.AuditLogAction.member_role_update:"🎭 Role Update",
                    discord.AuditLogAction.channel_delete:"🗑️ Channel Delete",
                    discord.AuditLogAction.role_delete:"🗑️ Role Delete"}
        try:
            async for entry in guild.audit_logs(limit=50):
                if entry.user.id==member.id and entry.action in alb:
                    al.append(f"{alb[entry.action]} → `{getattr(entry.target,'name',str(entry.target))}` <t:{int(entry.created_at.timestamp())}:R>")
                    if len(al)>=8: break
        except: pass
        e=discord.Embed(title=f"🔍 Scan — {member.display_name}",
            color=discord.Color.dark_red() if (age<ALT_ACCOUNT_AGE_DAYS or member.guild_permissions.administrator) else discord.Color.blurple(),
            timestamp=discord.utils.utcnow())
        e.set_thumbnail(url=member.display_avatar.url)
        e.add_field(name="👤 Χρήστης",       value=f"{member} (`{member.id}`)", inline=True)
        e.add_field(name="📅 Ηλικία",        value=f"{age} ημέρες {'⚠️ Πιθανό ALT' if age<ALT_ACCOUNT_AGE_DAYS else '✅'}", inline=True)
        e.add_field(name="📆 Δημιουργήθηκε", value=f"<t:{int(member.created_at.timestamp())}:F>", inline=True)
        e.add_field(name="🔑 Permissions",
            value=f"Administrator: {'✅' if member.guild_permissions.administrator else '❌'}\nBan: {'✅' if member.guild_permissions.ban_members else '❌'}\nKick: {'✅' if member.guild_permissions.kick_members else '❌'}\nManage Guild: {'✅' if member.guild_permissions.manage_guild else '❌'}",
            inline=True)
        e.add_field(name="🎭 Ρόλοι",         value=", ".join(r.mention for r in member.roles[1:]) or "Κανένας", inline=False)
        e.add_field(name=f"📋 Τελευταίες Ενέργειες ({len(al)})", value="\n".join(al) if al else "Καμία", inline=False)
        e.set_footer(text="Glorious Elas • Scan")
        await ctx.send(embed=e); return
    admins=[]; newa=[]; bl=[]; sus=[]
    for m in guild.members:
        age=(datetime.datetime.utcnow()-m.created_at.replace(tzinfo=None)).days
        if m.bot:
            iv=bool(m.public_flags and discord.PublicUserFlags.verified_bot in m.public_flags)
            bl.append(f"{'✅' if iv else '⚠️'} {m.mention} (`{m.id}`)")
        if not m.bot and m.guild_permissions.administrator: admins.append(f"{m.mention} (`{m.id}`)")
        if not m.bot and age<ALT_ACCOUNT_AGE_DAYS: newa.append(f"{m.mention} — {age} ημέρες")
        if not m.bot and m.guild_permissions.administrator and age<ALT_ACCOUNT_AGE_DAYS: sus.append(f"🚨 {m.mention} — Admin + {age} ημέρες")
    e=discord.Embed(title=f"🔍 Server Scan — {guild.name}", color=discord.Color.dark_orange(), timestamp=discord.utils.utcnow())
    e.add_field(name=f"👑 Administrators ({len(admins)})",                     value="\n".join(admins[:10]) or "Κανένας", inline=False)
    e.add_field(name=f"🤖 Bots ({len(bl)}) ✅/⚠️",                           value="\n".join(bl[:10])     or "Κανένα",  inline=False)
    e.add_field(name=f"⚠️ Νέοι < {ALT_ACCOUNT_AGE_DAYS} ημέρες ({len(newa)})",value="\n".join(newa[:10])   or "Κανένας", inline=False)
    e.add_field(name=f"🚨 Ύποπτα ({len(sus)})",                               value="\n".join(sus[:10])    or "✅ Τίποτα",inline=False)
    e.set_footer(text=f"Glorious Elas • Scan | {guild.member_count} μέλη")
    await ctx.send(embed=e)

# ── Owner + Co-Owner + Founder ────────────────────────────────
@bot.command()
async def say(ctx, *, message: str):
    if not is_owner_or_above(ctx.author): return await ctx.reply("❌ Μόνο Owner/Co-Owner/Founder.")
    await ctx.send(message)
    try: await ctx.message.delete()
    except: pass

@bot.command()
async def say2(ctx, *, message: str):
    if not is_owner_or_above(ctx.author): return await ctx.reply("❌ Μόνο Owner/Co-Owner/Founder.")
    guild=ctx.guild
    e=discord.Embed(description=message, color=discord.Color.from_rgb(20,20,40), timestamp=discord.utils.utcnow())
    if guild.icon: e.set_thumbnail(url=guild.icon.url)
    e.set_footer(text=guild.name, icon_url=guild.icon.url if guild.icon else None)
    await ctx.send(embed=e)
    try: await ctx.message.delete()
    except: pass

# ── Founder Only ──────────────────────────────────────────────
@bot.command()
async def setaltdays(ctx, days: int=None):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    global ALT_ACCOUNT_AGE_DAYS
    if not days or days<1: return await ctx.reply(f"Τρέχον όριο: **{ALT_ACCOUNT_AGE_DAYS} ημέρες**\nΧρήση: `!setaltdays <ημέρες>`")
    ALT_ACCOUNT_AGE_DAYS=days; await ctx.reply(f"✅ Νέο όριο: **{days} ημέρες**")

@bot.command()
async def togglealtban(ctx):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    global ALT_AUTO_KICK
    ALT_AUTO_KICK=not ALT_AUTO_KICK
    await ctx.reply(f"Alt auto-kick: {'✅ **Ενεργό**' if ALT_AUTO_KICK else '❌ **Ανενεργό**'}")

@bot.command()
async def lockapplication(ctx, app_type: str=None):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    valid=["whitelist","staff","manager","all"]
    if not app_type or app_type.lower() not in valid:
        status=""
        for t in ["whitelist","staff","manager"]:
            status+=f"{'🔒' if t in locked_applications else '🔓'} **{t.capitalize()}**\n"
        e=discord.Embed(title="🔒 Application Lock Status", description=status, color=discord.Color.blurple())
        e.set_footer(text="Χρήση: !lockapplication <whitelist/staff/manager/all>")
        return await ctx.reply(embed=e)
    app_type=app_type.lower()
    targets=["whitelist","staff","manager"] if app_type=="all" else [app_type]
    toggled=[]
    for t in targets:
        if t in locked_applications: locked_applications.remove(t); toggled.append(f"🔓 **{t.capitalize()}** — Ανοιχτό")
        else: locked_applications.add(t); toggled.append(f"🔒 **{t.capitalize()}** — Κλειστό")
    e=discord.Embed(title="🔒 Application Lock Αλλαγή", description="\n".join(toggled), color=discord.Color.orange(), timestamp=discord.utils.utcnow())
    e.set_footer(text=f"Από: {ctx.author}")
    await ctx.reply(embed=e)

@bot.command()
async def ticketpanel(ctx):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    e=discord.Embed(title="Glorious Elas — Support Panel",
        description="**Επίλεξε κατηγορία για να ανοίξεις ticket.**\n\n👑 **Ανώτατη Διοίκηση** — Επικοινωνία με Διοίκηση\n💬 **Support** — Γενική υποστήριξη\n📋 **Other** — Άλλο αίτημα\n\n*One active ticket at a time.*",
        color=discord.Color.from_rgb(20,20,40))
    e.set_image(url=BANNER_SUPPORT); e.set_thumbnail(url=SERVER_THUMBNAIL_URL)
    e.set_footer(text="Glorious Elas • Support System")
    await ctx.send(embed=e, view=MainTicketPanel()); await ctx.reply("Panel στάλθηκε.", delete_after=2)

@bot.command()
async def jobpanel(ctx):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    e=discord.Embed(title="Glorious Elas — Job Panel",
        description="**Επίλεξε υπηρεσία για αίτηση.**\n\n👮 **Ελληνική Αστυνομία**\n⚓ **Λιμενικό**\n\n*One active ticket at a time.*",
        color=discord.Color.from_rgb(20,20,40))
    e.set_image(url=BANNER_JOB); e.set_thumbnail(url=SERVER_THUMBNAIL_URL)
    e.set_footer(text="Glorious Elas • Job System")
    await ctx.send(embed=e, view=JobTicketPanel()); await ctx.reply("Panel στάλθηκε.", delete_after=2)

@bot.command()
async def donatepanel(ctx):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    e=discord.Embed(title="💎 Glorious Elas — Donate",
        description="**Θέλεις να κάνεις donate και να στηρίξεις τον server;**\n\nΠάτα το παρακάτω μενού για να ανοίξεις ticket!\nΗ ομάδα μας θα σε εξυπηρετήσει σύντομα.\n\n*One active ticket at a time.*",
        color=discord.Color.gold())
    e.set_image(url=BANNER_DONATE); e.set_thumbnail(url=SERVER_THUMBNAIL_URL)
    e.set_footer(text="Glorious Elas • Donate System")
    await ctx.send(embed=e, view=DonateTicketPanel()); await ctx.reply("Panel στάλθηκε.", delete_after=2)

@bot.command()
async def applicationpanel(ctx):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    lock_info=""
    for t in ["whitelist","staff","manager"]:
        lock_info+=f"{'🔒' if t in locked_applications else '🔓'} {t.capitalize()}  "
    e=discord.Embed(title="📋 Glorious Elas — Applications",
        description=f"**Επίλεξε τύπο αίτησης.**\n\n📋 **Whitelist**\n👮 **Staff**\n👔 **Manager**\n\n*Μία ενεργή αίτηση κάθε φορά.*\n\n{lock_info}",
        color=discord.Color.from_rgb(20,20,40))
    e.set_image(url=BANNER_APP); e.set_thumbnail(url=SERVER_THUMBNAIL_URL)
    e.set_footer(text="Glorious Elas • Applications")
    await ctx.send(embed=e, view=UnifiedApplicationPanel()); await ctx.reply("Panel στάλθηκε.", delete_after=2)

@bot.command()
async def whitelistpanel(ctx):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    await ctx.reply("ℹ️ Χρησιμοποίησε `!applicationpanel`!", delete_after=5)

@bot.command()
async def staffpanel(ctx):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    await ctx.reply("ℹ️ Χρησιμοποίησε `!applicationpanel`!", delete_after=5)

@bot.command()
async def managerpanel(ctx):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    await ctx.reply("ℹ️ Χρησιμοποίησε `!applicationpanel`!", delete_after=5)

@bot.command()
async def dutypanel(ctx):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    e=discord.Embed(title="🟢 Staff Duty Panel",
        description="Πάτα **On Duty** όταν ξεκινάς βάρδια και **Off Duty** όταν τελειώνεις.\n\n"
                    "📋 **Duty Status** — Δες ποιοι είναι on duty τώρα\n"
                    "🏆 **Leaderboard** — Συνολικές ώρες",
        color=discord.Color.green())
    await ctx.send(embed=e, view=DutyView()); await ctx.reply("Panel στάλθηκε.", delete_after=2)

@bot.command()
async def suggestionpanel(ctx):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    e=discord.Embed(title="💡 Glorious Elas — Suggestions", description="**Έχεις πρόταση;**\nΠάτα το κουμπί, γράψε και στείλε!\nΗ κοινότητα ψηφίζει 👍 / 👎", color=discord.Color.from_rgb(88,101,242))
    e.set_image(url=BANNER_SUGGEST); e.set_thumbnail(url=SERVER_THUMBNAIL_URL)
    e.set_footer(text="Glorious Elas • Suggestion System")
    await ctx.send(embed=e, view=SuggestionPanelView()); await ctx.reply("Panel στάλθηκε.", delete_after=2)

@bot.command()
async def reviewpanel(ctx):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    e=discord.Embed(title="⭐ Glorious Elas — Reviews", description="**Πώς σου φαίνεται ο server;**\nΠάτα, επίλεξε αστέρια (1-5) και γράψε σχόλιο!", color=discord.Color.from_rgb(255,215,0))
    e.set_image(url=BANNER_REVIEW); e.set_thumbnail(url=SERVER_THUMBNAIL_URL)
    e.set_footer(text="Glorious Elas • Review System")
    await ctx.send(embed=e, view=ReviewPanelView()); await ctx.reply("Panel στάλθηκε.", delete_after=2)

# ── !panel — Founder ──────────────────────────────────────────
@bot.command()
async def panel(ctx):
    if not is_founder(ctx.author): return await ctx.reply("❌ Μόνο Founder.")
    e=discord.Embed(title="📌 Glorious Elas — Founder Panel", color=discord.Color.dark_gray(), timestamp=discord.utils.utcnow())
    e.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else None)
    e.add_field(name="🛠 Moderation",   value="`!ban` `!kick` `!timeout` `!clearmessage`", inline=False)
    e.add_field(name="📊 Info",         value="`!serverstatus` `!invites [@user]` `!serverinvites` `!scan [@user]`", inline=False)
    e.add_field(name="🧰 Utility",      value="`!say <msg>` `!say2 <msg>`", inline=False)
    e.add_field(name="🔍 Security",     value="`!setaltdays <days>` `!togglealtban`", inline=False)
    e.add_field(name="📋 Applications", value="`!applicationpanel` `!lockapplication <type>`", inline=False)
    e.add_field(name="🎫 Panels",       value="`!ticketpanel` `!jobpanel` `!donatepanel` `!suggestionpanel` `!reviewpanel` `!dutypanel`", inline=False)
    e.set_footer(text=f"Glorious Elas • Founder Panel | {ctx.author}")
    await ctx.reply(embed=e)

# ── !panel2 — Owner/Co-Owner + Founder ───────────────────────
@bot.command()
async def panel2(ctx):
    if not is_owner_or_above(ctx.author): return await ctx.reply("❌ Μόνο Owner/Co-Owner/Founder.")
    e=discord.Embed(title="📌 Glorious Elas — Owner Panel", color=discord.Color.gold(), timestamp=discord.utils.utcnow())
    e.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else None)
    e.add_field(name="🛠 Moderation",  value="`!ban @user [λόγος]`\n`!kick @user [λόγος]`\n`!timeout @user <minutes> [λόγος]`\n`!clearmessage <amount>`", inline=False)
    e.add_field(name="📊 Info",        value="`!serverstatus`\n`!invites [@user]`\n`!serverinvites`\n`!scan [@user]`", inline=False)
    e.add_field(name="🧰 Utility",     value="`!say <msg>`\n`!say2 <msg>`", inline=False)
    e.set_footer(text=f"Glorious Elas • Owner Panel | {ctx.author}")
    await ctx.reply(embed=e)

# ── !panel3 — Staff/Manager ───────────────────────────────────
@bot.command()
async def panel3(ctx):
    if not is_staff_or_manager(ctx.author): return await ctx.reply("❌ Δεν έχεις δικαίωμα.")
    e=discord.Embed(title="📌 Glorious Elas — Staff Panel", color=discord.Color.blurple(), timestamp=discord.utils.utcnow())
    e.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else None)
    e.add_field(name="🛠 Moderation",  value="`!ban @user [λόγος]`\n`!kick @user [λόγος]`\n`!timeout @user <minutes> [λόγος]`\n`!clearmessage <amount>`", inline=False)
    e.add_field(name="📊 Info",        value="`!serverstatus`\n`!invites [@user]`\n`!serverinvites`\n`!scan [@user]`", inline=False)
    e.set_footer(text=f"Glorious Elas • Staff Panel | {ctx.author}")
    await ctx.reply(embed=e)

# ══════════════════════════════════════════════════════════════
#  ON READY
# ══════════════════════════════════════════════════════════════
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    for v in [MainTicketPanel(), JobTicketPanel(), DonateTicketPanel(), TicketCloseView(),
              DutyView(), UnifiedApplicationPanel(), SuggestionPanelView(), ReviewPanelView(), StarSelectView()]:
        bot.add_view(v)
    guild=bot.get_guild(GUILD_ID)
    if guild:
        await update_voice_channels(guild)
        try:
            invs=await guild.invites()
            invite_cache[guild.id]={i.code:i.uses for i in invs}
            print(f"Loaded {len(invs)} invites into cache.")
        except Exception as e: print(f"Invites error: {e}")
    await bot.change_presence(activity=discord.Game(name="Glorious Elas"))
    print("Bot fully online!")

if __name__=="__main__":
    keep_alive()
    bot.run(TOKEN)
