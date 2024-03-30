const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

console.log('\n--------CPU Scheduling--------')
console.log('First Come First Served (FCFS)')
console.log('Shortest Job First (SJF)')
console.log('Shortest Remaining Time (SRT)')
console.log('Round Robin (RR)')
console.log('Priority Scheduling (PS)')
console.log('------------------------------')



rl.question('Please enter your desired cpu scheduling: ', (cpuScheduling) => {
  const chosenCpuScheduling = cpuScheduling === 'FCFS' ? 'First Come First Served' : 
                              cpuScheduling === 'SJF' ? 'Shortest Job First' : 
                              cpuScheduling === 'SRT' ? 'Shortest Remaining Time' :
                              cpuScheduling === 'RR' ? 'Round Robin' :
                              cpuScheduling === 'PS' ? 'Priority Scheduling' : 
                              null
  if (chosenCpuScheduling) {
    console.log(`You've chosen: ${chosenCpuScheduling}\n`);
  } else {
    console.log('Invalid Input. Try again.\n')
  }

  rl.close();
});


function computeFCFS() {
  rl.question('Enter the number of processes: ', (processes) => {
    // Arrival time
    console.log('Enter the arrival times')
    for (let i = 0; i < processes; i++) {
      rl.question(`P${i + 1}: `, () => {
        
      })
    }
    // Burst time
    console.log('Enter the burst times')
    for (let i = 0; i < processes; i++) {
      rl.question(`P${i + 1}: `, () => {

      })
    }
  })
}