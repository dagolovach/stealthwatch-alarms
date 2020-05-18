from collections import OrderedDict
import json

def generate_json():
    """Function to generate json file baes on alarms_src.txt file
    """
    alarms = OrderedDict()
    with open('alarms_src.txt', 'r') as f:
        content = f.read()
        alerts = content.split('+++')
        for each in alerts:
            details = each.split('\n')
            name = details[0].split(': ', 1)[1]
            mitigation = details[1].split(': ', 1)[1]
            meaning = details[2].split(': ', 1)[1]
            meaning_list = meaning.split('###')
            meaning_str = '\n'.join(meaning_list)
            steps = details[3].split(': ', 1)[1]
            steps_list = steps.split('###')
            steps_str = '\n'.join(steps_list)
            alarms[name.lower()] = {
                'name': name,
                'mitigation': mitigation,
                'meaning': meaning_str,
                'steps': steps_str
            }
    
    with open('alarms.json', 'w') as outfile:
        json.dump(alarms, outfile)

# Run main function
if __name__ == "__main__":
    generate_json()
