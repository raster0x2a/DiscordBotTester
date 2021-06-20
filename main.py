import asyncio

import requests
import PySimpleGUI as sg


async def send_message(token, channel_id, content):
    url = f"https://discordapp.com/api/channels/{channel_id}/messages"
    data = f'{{"content": "{content}" }}'
    headers = {
        "authorization": f"Bot {token}",
        "content-type": "application/json"
    }

    response = requests.post(url, data, headers=headers)
    print(response, response.text)

    return response

async def main():
    sg.theme('Dark Blue 14')

    layout = [
        [sg.Text('DiscordBotTester')],
        [sg.Text('token', size=(15, 1)), sg.InputText("", key="-token-")],
        [sg.Text('channel id', size=(15, 1)), sg.InputText('', key="-channel_id-")],
        [sg.Text('content', size=(15, 1)), sg.InputText('', key="-content-")],
        [sg.Text("", size=(15, 1), key="-output-")],
        [sg.Submit(button_text='send'), sg.Submit(button_text='close')]
    ]

    window = sg.Window('title', layout)

    while True:
        event, values = window.read()

        if event is None or event == "close":
            print('exit')
            break

        if event == 'send':
            print("send")

            # send message
            token = values["-token-"]
            channel_id = values["-channel_id-"]
            content = values["-content-"]
            result = await send_message(token, channel_id, content)

            if result.status_code == 200:
                print("Successful")
                window["-output-"].update("Successful", text_color='blue')
            else:
                print("ERROR")
                window["-output-"].update("Error", text_color='red')
                
            #sg.popup("send")

    window.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
