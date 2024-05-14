![outage](https://github.com/J-VIEW/alx-system_engineering-devops/assets/106552716/90d563e2-4c2f-4de1-85e6-dc1745d50a0b)
Duration: The outage occurred from 2:00 AM to 5:30 AM UTC on May 12, 2024 (3 hours and 30 minutes).
Impact: Our web application was down and inaccessible to all users during this period. This affected 100% of our user base, which consists of approximately 2 million active users worldwide.
Root Cause: The outage was caused by an unexpected spike in traffic due to a viral social media post mentioning our service, which overloaded our servers and caused them to crash.
Timeline

2:00 AM UTC - The outage began, and our monitoring system triggered an alert.
2:15 AM UTC - The on-call engineer was notified and began investigating the issue.
2:30 AM UTC - The engineer noticed that the web servers were unresponsive and restarted them, but the issue persisted.
3:00 AM UTC - The engineer assumed it was a database issue and began investigating the database servers.
3:30 AM UTC - After ruling out the database, the engineer escalated the issue to the infrastructure team.
4:00 AM UTC - The infrastructure team identified the spike in traffic as the root cause and began provisioning additional servers to handle the load.
5:00 AM UTC - The new servers were brought online, and the application was slowly recovering.
5:30 AM UTC - The application was fully restored, and the outage was resolved.

Root Cause and Resolution
The root cause of the outage was an unexpected spike in traffic due to a viral social media post mentioning our service. Our existing server infrastructure was not designed to handle such a sudden and massive influx of users, leading to the servers becoming overloaded and crashing.
To resolve the issue, the infrastructure team provisioned additional servers and load balancers to distribute the traffic more effectively. Once the new servers were online and the load was balanced, the application was able to handle the increased traffic, and the outage was resolved.
Corrective and Preventative Measures
Areas for Improvement:

Improve our capacity planning and scalability to handle sudden spikes in traffic.
Enhance monitoring and alerting systems to detect traffic anomalies earlier.
Implement auto-scaling mechanisms to automatically provision additional resources during high traffic periods.

TODO Tasks:

Implement auto-scaling groups for web servers and load balancers.
Configure monitoring alerts for sudden traffic spikes and high resource utilization.
Conduct load testing and capacity planning exercises regularly.
Develop a runbook for handling traffic spikes and server overload scenarios.
Investigate the use of a content delivery network (CDN) to offload static content and improve performance during high traffic periods.

