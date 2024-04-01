
def get_user_input():
  try:
    processes = int(input("Enter the number of processes: "))

    #Print the values
    print('P        AT        BT')
    for i in range(1, processes + 1):
      print(f'P{i}')

    arrival_times = []
    print('\nEnter the arrival times: ')
    for i in range(1, processes + 1):
      arrival_time = int(input((': ')))
      arrival_times.append(arrival_time)
    
    burst_times = []
    print('\nEnter the burst times: ')
    for i in range(1, processes + 1):
      burst_time = int(input(': '))
      burst_times.append(burst_time)

    return processes, arrival_times, burst_times

  except ValueError:
    print('Input is not a number. Try again.\n')


def display_output_table(chosen_cpu_scheduling):
  processes, arrival_times, burst_times, completion_time, turnaround_time, waiting_time = compute_fcfs()

  print(f'\n{chosen_cpu_scheduling}')
  print('-------------------------------')
  print('P        AT        BT        CT        TAT        WT')
  for i in range(1, processes + 1):
    print(f'P{i}        {arrival_times[i - 1]}        {burst_times[i - 1]}         {completion_time[i - 1]}        {turnaround_time[i - 1]}        {waiting_time[i - 1]}')


def compute_fcfs(): 
  processes, arrival_times, burst_times = get_user_input()

  sorted_processes = sorted(zip(arrival_times, burst_times), key=lambda x: x[0])
  arrival_times, burst_times = zip(*sorted_processes)

  completion_time = [0] * processes
  completion_time[0] = arrival_times[0] + burst_times[0]
  for i in range(1, processes):
    completion_time[i] = completion_time[i - 1] + burst_times[i]

  turnaround_time = [0] * processes
  for i in range(processes):
    turnaround_time[i] = completion_time[i] - arrival_times[i]

  waiting_time = [0] * processes
  for i in range(processes):
    waiting_time[i] = turnaround_time[i] - burst_times[i]

  return processes, arrival_times, burst_times, completion_time, turnaround_time, waiting_time






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


if (chosen_cpu_scheduling):
  print(f'You have chosen: {chosen_cpu_scheduling}\n')
  display_output_table(chosen_cpu_scheduling)
else:
  print('Invalid input. Try again.')

