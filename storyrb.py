import stdiomask, secrets, uuid, os
import requests, time
from user_agent import *


done = 0
error = 0
guid = str(uuid.uuid1())
tags = ['ig_self_injury_v3','ig_nudity_or_pornography_v3','ig_hate_speech_v3','ig_bullying_or_harassment_me_v3']

banner =( """
        _____                       _ _  
        |  __ \                     | |  
        | |__) |___ _ __   ___  _ __| |_ 
        |  _  // _ \ '_ \ / _ \| '__| __|
        | | \ \  __/ |_) | (_) | |  | |_ 
        |_|  \_\___| .__/ \___/|_|   \__|
                    | |                   
                    |_|                   
  
    ~Mass Story reporter by @crackled on tele~                                                                                       
""")



def story_report(mediaid):
    global done, error
    headers = {'Cookie': 'sessionid=' + r.cookies.get_dict()['sessionid'],'User-Agent': 'Instagram 184.0.0.30.117 Android (30/11; 480dpi; 1080x2158; OPPO; CPH2069; OP4C7BL1; qcom; en_US; 285855788)','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    for tag in tags:
        url = 'https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_policy_education/'
        params = '%7B%22server_params%22%3A%7B%22selected_option%22%3A%22report%22%2C%22serialized_state%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_story%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22e5e4a6f6-b4ad-4a46-9f2b-18ced58703ef%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22' + tag + '%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22media_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22' + mediaid + '%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400363363986%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841401175190745%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A0%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22reel_feed_timeline%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22184.0.0.30.117%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A567067343352427%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%2C%5C%5C%5C%22tag_source%5C%5C%5C%22%3A%5C%5C%5C%22tag_selection_screen%5C%5C%5C%22%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_policy_education%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22reel_feed_timeline%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%2283519563-16da-460d-aca5-2a49c0d927ce%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%7D%7D'
        data = 'params=' + params + '&_uuid=a4b3a866-b663-4fce-9dec-6b5f7e8bf9a5&bk_client_context=%7B%22bloks_version%22%3A%22befa8522d3a650f9592e33e4540d527c5b93babbdd6233a1bd40e955c9567f30%22%2C%22styles_id%22%3A%22instagram%22%7D&nest_data_manifest=true&bloks_versioning_id=befa8522d3a650f9592e33e4540d527c5b93babbdd6233a1bd40e955c9567f30'
        res = r.post(url, headers=headers, data=data)
        if res.status_code == 200:
            done+=1
        else:
            error+=1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(banner)
        tagg = tag.split("_")[1]
        print(f"==========================================\nSent: {done} \nErrors: {error} \nReporting: @{usr} stories For {tagg}\n==========================================\n ")
        time.sleep(sle)


def GetMediaID(targetID):
    stories = []
    headers = {'User-Agent': 'Instagram 177.0.0.30.119 Android (30/11; 480dpi; 1080x2158; OPPO; CPH2069; OP4C7BL1; qcom; en_US; 276028020)',}
    url ="https://i.instagram.com/api/v1/feed/user/" + targetID + "/story/"
    response = r.get(url, headers=headers)
    if response.status_code == 200:
        for item in response.json()['reel']['items']:
            stories.append(str(item['pk']))
        print(f'[DONE] Fetched {len(stories)} Stories For {usr}')
        return stories
    else:
        print(f'[ERROR] Error Fetching Stories')
        


def GetTargetID(usr):
    try:
        graph = r.get(f'https://instagram.com/{usr}/?__a=1').json()
        targetID = graph['logging_page_id'].split('_')[1]
        return targetID
    except:
        return False



def login():
    global usr , done, error, sle, r
    r = requests.session()
    username = input('\n[+] Username: ')
    passwd = stdiomask.getpass('[+] Password: ')
    headers = {'User-Agent': 'Instagram 9.4.0 Android (30/11; 480dpi; 1080x2158; OPPO; CPH2069; OP4C7BL1; qcom; en_US; 276028020)', "Content-Type": "application/x-www-form-urlencoded","X-CSRFToken": "uNs1OZ6CPvJBSmmQOvWDKGFkm2frIDEY"}
    data = "username=" + username + "&password=" + passwd + "&device_id=android-" +  secrets.token_hex(8) +"&_csrftoken=2C3OWk1zw20DXvUj3lr7YT8nCEgGmJJq&phone_id=" + guid + "&guid=" + guid
    response = r.post('https://b.i.instagram.com/api/v1/accounts/login/', headers=headers, data=data)
    try:
        response.cookies['sessionid']
        print('\n[SUCCESS] Logged In!')
        time.sleep(2)
        while True:
            try:
                done = 0
                error = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                print(banner)
                usr = input("[+] Target User: ")
                sle = int(input("[+] Sleep Between Reports: "))
                targetID = GetTargetID(usr)
                if isinstance(targetID, str):
                    try:
                        stories = GetMediaID(targetID)
                        for item in stories:
                            story_report(item)

                        print('[DONE] All reports have been sent! ')
                        time.sleep(5)
                    except (KeyError, TypeError):
                        print('[ERROR] No stories found.')
                        time.sleep(5)
                else:
                    print('[ERROR] User: {} Not Found.'.format(usr))
            except KeyboardInterrupt:
                return
            except:
                 print('[ERROR] Something went wrong.')
                 time.sleep(5)
    except:
        if "The password you entered is incorrect."in response.text:
            print('\n[ERROR] Password Incorrect')
            time.sleep(5)
        elif "The username you entered doesn't appear to belong to an account." in response.text:
            print('\n[ERROR] User does not exist')
            time.sleep(5)
            
        elif "Invalid Parameters" in response.text:
            print('\n[ERROR] Invalid Inputs')
            time.sleep(5)
        else:
            print(f'[ERROR] Check Your Account For a Checkpoint')
            time.sleep(5)


def login2():
    global r, usr, sle
    usr = input("[+] Target User: ")
    sle = int(input("[+] Sleep: "))
    file = open('Accounts.txt', 'r').read().splitlines()
    try:
        for line in file:
        
            r = requests.session()
            username = line.split(':')[0]
            passwd = line.split(':')[1]
            headers = {'User-Agent': 'Instagram 9.4.0 Android (30/11; 480dpi; 1080x2158; OPPO; CPH2069; OP4C7BL1; qcom; en_US; 276028020)', "Content-Type": "application/x-www-form-urlencoded", "X-CSRFToken": "uNs1OZ6CPvJBSmmQOvWDKGFkm2frIDEY"}
            data = "username=" + username + "&password=" + passwd + "&device_id=android-" +  secrets.token_hex(8) +"&_csrftoken=2C3OWk1zw20DXvUj3lr7YT8nCEgGmJJq&phone_id=" + guid + "&guid=" + guid
            response = r.post('https://b.i.instagram.com/api/v1/accounts/login/', headers=headers, data=data)
            if response.status_code == 200:
                print('\n[SUCCESS] Logged In!')
                response.cookies['sessionid']
                targetID = GetTargetID(usr)
                if isinstance(targetID, str):
                    try:
                        stories = GetMediaID(targetID)
                        for item in stories:
                            story_report(item)

                    except (KeyError, TypeError):
                        print('[ERROR] No stories found.')
                        time.sleep(5)
                else:
                    print('[ERROR] User: {} Not Found.'.format(usr))
                
            else:
                print('[LOGIN ERROR] Could not login to {} '.format(username))
                time.sleep(1)
                continue
        
        print('[DONE] All reports have been sent! ')
        time.sleep(5)
        
    except KeyboardInterrupt:
        return
    except:
        print('[ERROR] Something went wrong.')
        time.sleep(9)



def panel():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(banner)
        choice = input("""
[1] Single Session Report
[2] Multi-Session Report

[+] Choose One: """)
        if choice == '1':
            login()
        elif choice == '2':
            login2()
        else:
            pass





if __name__ == "__main__":
    panel()
