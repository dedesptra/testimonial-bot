import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime

TOKEN = "MTQ1ODg1MTk3NTY1ODYwMjQ5Ng.G12YDc.dGm8419fXB-sW7ddeFmhUxl8N_y9VVEz9pngnk"
TARGET_CHANNEL_ID = 1459078280933146744  # GANTI CHANNEL ID

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

<@&1459023594448224288>.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot aktif sebagai {bot.user}")

<@&1459023594448224288>.tree.command(name="testimonial", description="Kirim testimonial + bukti transaksi")
@app_commands.describe(
    seller="Username seller",
    buyer="Mention buyer (@user)",
    product="Produk",
    price="Harga",
    payment="Metode pembayaran",
    bukti="Upload bukti transaksi (gambar)"
)
async def testimonial(
    interaction: discord.Interaction,
    seller: str,
    buyer: discord.Member,  # agar bisa mention asli
    product: str,
    price: str,
    payment: str,
    bukti: discord.Attachment
):

    # Validasi file harus gambar
    if not bukti.content_type.startswith("image"):
        await interaction.response.send_message(
            "❌ File harus berupa gambar!", 
            ephemeral=True
        )
        return

    # Ambil channel tujuan
    channel = bot.get_channel(1459078280933146744)

    if channel is None:
        await interaction.response.send_message(
            "❌ Channel tidak ditemukan!", 
            ephemeral=True
        )
        return

    embed = discord.Embed(
        title="📢 NYT MARKET #1 Termurah",
        color=discord.Color.dark_red()
    )

    embed.add_field(name="👤 Seller", value=f"@{seller}", inline=False)
    embed.add_field(name="⚡ Buyer", value=buyer.mention, inline=False)
    embed.add_field(name="🛒 Product", value=product, inline=False)
    embed.add_field(name="💰 Price", value=f"Rp {price}", inline=False)
    embed.add_field(name="💳 Payment Method", value=payment, inline=False)

    embed.set_image(url=bukti.url)
    embed.set_footer(text="💎 Premium Quality • Trusted Service • Fast Delivery")
    embed.timestamp = datetime.utcnow()

    # Kirim ke channel khusus
    await channel.send(embed=embed)

    # Balasan ke user yang pakai command
    await interaction.response.send_message(
        "✅ Testimonial berhasil dikirim ke channel!",
        ephemeral=True
    )

bot.run(TOKEN)
