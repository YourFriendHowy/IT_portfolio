| Term         | Explanation                                                           |
| ------------ | --------------------------------------------------------------------- |
| Load Average | Number of processes waiting for CPU time                              |
| Values       | 3 numbers: 1-minute, 5-minute, and 15-minute averages                 |
| Source       | Displayed by `uptime` and stored in `/proc/loadavg`                   |
| Meaning      | On a single-core system, 1.00 = full CPU usage (no idle); over = wait |s

## Example 
14:32:01 up 3 days,  4:27,  2 users,  load average: 0.58, 0.40, 0.36

'0.** ' Load shows how many tasks are waiting on the cpu