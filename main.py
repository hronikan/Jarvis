#Jarvis v0.1
import os
import random
import speech_recognition
import pyttsx3

engine = pyttsx3.init()

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5


ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"

engine.setProperty('voice', ru_voice_id) 

engine.setProperty('rate', 250)     


commands_dict = {
    'commands': {
        'greeting': ('привет', 'приветствую', 'привет джарвис'),
        'create_task': ('добавить задачу', 'создать задачу', 'заметка'),
        'play_music': ('включить музыку', 'включи музыку', 'дискотека'),
        'off': ('выключись', 'выключить', 'пока', 'стоп')
    }
}

def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source = mic, duration = 0.5)
            audio = sr.listen(source = mic)
            query = sr.recognize_google(audio_data = audio, language = 'ru-RU').lower()

        return query
    except speech_recognition.UnknownValueError:
        return 



def greeting():
    engine.say('Здравствуйте, Сэр!')
    engine.runAndWait()
    return 'Здравствуйте, Сэр!'

def create_task():

    engine.say('Что добавим в список дел?')
    engine.runAndWait()

    print('Что добавим в список дел?')
    
    query = listen_command()

    with open('todo-list.txt', 'a') as file:
        file.write(f'{query}\n')

    engine.say(f'Задача {query} добавлена!')
    engine.runAndWait()

    return f'Задача {query} добавлена в todo-list!'


def play_music():
    # Play a random mp3 file

    files = os.listdir('D:\music')
    random_file = f'D:\music\{random.choice(files)}'
    os.startfile(f'{random_file}')

    engine.say('Ща будет мясо')
    engine.runAndWait()

    return f'Танцуем под {random_file.split("/")[-1]}'


def off():
    engine.say('Досвидания!')
    engine.runAndWait()
    return 'Досвидания!', quit()
    


def main():
    query = listen_command()
    print(query)

    for k, v in commands_dict['commands'].items():
        if query in v:
            print(globals()[k]())


while True:
    if __name__ == '__main__':
        main()