print('\n--------CPU Scheduling--------')
print('First Come First Served (FCFS)')
print('Shortest Job First (SJF)')
print('Shortest Remaining Time (SRT)')
print('Round Robin (RR)')
print('Priority Scheduling (PS)')
print('------------------------------')

user_choice = input('Please enter your desired cpu scheduling: ')

cpu_scheduling_mappings = {
  'FCFS': 'First Come First Served',
  'SJF': 'Shortest Job First',
  'SRT': 'Shortest Remaining Time',
  'RR': 'Round Robin',
  'PR': 'Priority Scheduling'
}

chosen_cpu_scheduling = cpu_scheduling_mappings.get(user_choice)


def getUserInput():
  try:
    processes = int(input("Enter the number of processes: "))

    #Print the values
    print('P        AT        BT')
    for i in range(1, processes + 1):
      print(f'P{i}')

    arrival_times = []
    print('\nEnter the arrival times: ')
    for i in range(1, processes + 1):
      arrival_time = int(input((f'P{i}: ')))
      arrival_times.append(arrival_time)
    
    burst_times = []
    print('\nEnter the burst times: ')
    for i in range(1, processes + 1):
      burst_time = int(input(f'P{i}: '))
      burst_times.append(burst_time)

    return processes, arrival_times, burst_times

  except ValueError:
    print('Input is not a number. Try again.\n')


def computeFCFS(): 
  processes, arrival_times, burst_times = getUserInput()
  print(f'Processes: {processes}')





if (chosen_cpu_scheduling):
  print(f'You have chosen: {chosen_cpu_scheduling}\n')
  computeFCFS()
else:
  print('Invalid input. Try again.')

