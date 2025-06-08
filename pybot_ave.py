def ave_command(command):
    data = command.split()
    command_args = data[1:]
    goukei = 0
    heikin = 0
    for num in command_args:
        goukei += int(num)
    heikin = goukei/2
    responce = '平均は「{}」です'.format(heikin)
    return responce
        
