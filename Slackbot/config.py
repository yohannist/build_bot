import re, json
from enum import Enum

build_key_pattern = re.compile(r'(build) (S2S|EMS)-(\d\d\d\d?)')

bot_name = ''
token = ''
bot_id = ''
bot_sleep_delay = ''
bamboo_plans_endpoint = ''
bamboo_queue_build_endpoint = ''
bamboo_uid = ''
bamboo_pwd = ''

loaded = False

def init():
    settings_file = open('./settings.json');
    settings = json.loads(settings_file.read());
    settings_file.close()

    bot_name = settings['slack']['botName']
    token = settings['slack']['token']
    bot_id = settings['slack']['id']
    bot_sleep_delay = settings['slack']['botNapTime']

    bamboo_plans_endpoint =  settings['bamboo']['plansEndpoint']
    bamboo_queue_build_endpoint = settings['bamboo']['queueBuildEndpoint']

    bamboo_uid = settings['bamboo']['auth']['uid']
    bamboo_pwd = settings['bamboo']['auth']['pwd']
    loaded = True

init();