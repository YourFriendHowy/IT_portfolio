---
obsidianUIMode: preview
Language:
  - N/A
Category: ComputerManagement
Topic:
  - EvenViewer
Type: Notes
System: Windows
Element type:
  - Concept
Arguments: N
Source:
  - TryHackMe.com
Complexity: Intermediate
Keywords:
  - Event Viewer
aliases:
DateCreated: 2025-11-06
LastEdited: 2025-11-06
---
>[!infobox]
> # `=this.file.name`
> Category |  Info |
> ---|---|
> System|`=this.System`
> Languages|`=this.Language`
> Topic|`=this.Topic`
> Source| `=this.Source`
> Last Edit|`=this.LastEdited`
> # Important
> -

# Event Viewer

Allows the user to view events that have occurred on the computer. It is a log of events that can be viewed and audited to understand any activity on the individual PC. The information can be used to investigate and diagnose problems or actions that have taken place on the system.


| Event Type    | Description                                                                                                                                                                                                                       |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Error         | An event that indicates a major problem has been encountered, such as loss of data or functionality. For example, if a service fails, en error will be logged as an event.                                                        |
| Warning       | An event that isn't seen as major, but could pose a potential problem in the future. IE, low disk space. If an application is able to recover from an issue w/o loss of data or functionality, its probably a warning type event. |
| Information   | These events showcase successful operation of an application, service, or driver. **Note:** It is not common for a desktop application to log a an event each time it starts.                                                     |
| Success Audit | An event that records a security audited access attempt that is successful, a successful user login                                                                                                                               |
| Failure Audit | An event that records a security audited access attempt that fails, if a user tries to access a network drive and fails, it is logged as a failed audit event                                                                     |

| Log Type    | Description                                                                                                                                                                                                         |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Application | Logs activity from programs or software. For example, if a database app crashes or throws a file error, it’ll show up here. Each app chooses what events it wants to record.                                        |
| Security    | Tracks things like valid or failed logins, and actions that touch files, permissions, or resources. Admins can enable auditing to record this data for investigation or compliance.                                 |
| System      | Logs system level events such as driver errors, failed hardware, or startup service issues. Basically, anything the OS itself is responsible for running or monitoring.                                             |
| Custom Log  | Used by apps that make their own log file. It lets them control log size, access permissions, or retention without messing with the main Windows logs. Handy for devs or security tools that track their own stuff. |
