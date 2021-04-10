import requests
import sys
import base64

def get_wave(fname):
    with open(fname, 'rb') as infile:
        return base64.b64encode(infile.read())

endpoint = 'http://127.0.0.1:8888/api/v1/train'

# print(str(get_wave('1.wav')))

data = {
    "name":"athena",
    "voice_samples":[
        { "wave": str(get_wave('1.wav'), 'ascii')},
        { "wave": str(get_wave("2.wav"), 'ascii')},
        { "wave": str(get_wave("3.wav"), 'ascii')}
    ],
    "language":"en"
}


x = requests.post(endpoint, json = data)

if x.ok:
    print('uhh baby fuck yea')
    with open('saved-model.pmdl', 'wb') as outfile: 
        outfile.write(x.content)
else:
    print('you fucking monkey messed up')
    print(x.status_code)
# print(x.text)


# import sys
# import base64
# import requests
# import json
#
#
# def get_wave(fname):
#     with open(fname) as infile:
#         return base64.b64encode(infile.read())
#
#
# endpoint = 'http://127.0.0.1:8888/api/v1/train'
#
#
# ############# MODIFY THE FOLLOWING #############
# token = ""
# hotword_name = "athena"
# language = "en"
# age_group = "20_29"
# gender = "M"
# microphone = ""
# ############### END OF MODIFY ##################
#
# if __name__ == "__main__":
#     try:
#         [_, wav1, wav2, wav3, out] = sys.argv
#     except ValueError:
#         print ("Usage: %s wave_file1 wave_file2 wave_file3 out_model_name" % sys.argv[0])
#         sys.exit()
#
#     data = {
#         "name": hotword_name,
#         "language": language,
#         "age_group": age_group,
#         "gender": gender,
#         "microphone": microphone,
#         "token": token,
#         "voice_samples": [
#             {"wave": str(get_wave(wav2), 'ascii', 'ignore')},
#             {"wave": get_wave(wav2)},
#             {"wave": get_wave(wav3)}
#         ]
#     }
#
#     response = requests.post(endpoint, json=json.dumps(data))
#     if response.ok:
#         with open(out, "w") as outfile:
#             outfile.write(response.content)
#         print("Saved model to '%s'.") % out
#     else:
#         print ("Request failed.")
#         print (response.text)
