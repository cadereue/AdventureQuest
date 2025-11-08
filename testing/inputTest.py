import player_settings_t

while True:
    player_input = input('input your answer').lower()
    if player_input == player_settings_t.player_name:
        print("success")
        break
    else:
        print('fail')
