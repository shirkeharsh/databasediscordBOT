import discord
from discord.ext import commands
import mysql.connector
import os
from dotenv import load_dotenv


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)



def get_db_connection():
  
    return mysql.connector.connect(
        host="localhost",  
        user="username", 
        password="passwordhere", 
        database="databasename" 
    )

def get_data_by_name(name):

    try:
        db_connection = get_db_connection()
        cursor = db_connection.cursor()
        query = "SELECT first_name, last_name, phone, email, course FROM user WHERE first_name = %s"
        cursor.execute(query, (name,))
        result = cursor.fetchall() 
        return result
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return None
    finally:
        db_connection.close()


def format_message(data):
   
    formatted_message = (
        f"**:bookmark_tabs: User Information**:\n"
        f"**:name_badge: Full Name:** {data[0]} {data[1]}\n"
        f"**:telephone: Phone:** {data[2]}\n"  
        f"**:envelope_with_arrow: Email:** {data[3]}\n"
        f"**:book: Course:** {data[4]}\n"
        f"------------------------\n"
    )
    return formatted_message



@bot.command()
async def get(ctx, name: str):
  
    data_by_name = get_data_by_name(name)

    
    if data_by_name:
        
        if len(data_by_name) > 1:
            await ctx.send(f"**:memo: Multiple users found for the name '{name}':**")
        for data in data_by_name:
            message = format_message(data)
            await ctx.send(message) 
    else:
        await ctx.send(f"**:warning: No data found for the name '{name}'**.")



if __name__ == "__main__":
    
    bot.run(os.getenv("DISCORD_BOT_TOKEN"))
