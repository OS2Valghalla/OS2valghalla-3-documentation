Queue and worker
===========

Valghalla is using RabbitMQ as a queue for different events, both the internal and the external application is acting on different queues. 
Then there is also Valghalla worker that is acting on some of the queues.

There are currently these different queues being used in the solution. 

* AuditLogClearJob. Run every 7 days / 168 hours to clear audit logs when users modify data and access participant as well as CPR service. Only logs that 6 months old will be deleted. The time can be configured in the settings.
* CommunicationLogClearJob. Run every 7 days / 168 hours to clear communication logs. Only logs that 4 months old will be deleted. The time can be configured in the settings.
* ElectionActivationJob. Run on demand when activate election to send communication messages to registered tasks. Timeout and retry period can be configured in the settings.
*	ElectionDeactivationJob. Runs every 7 days / 168 hours to check if election end date is already passed. If the date is passed the election will be deactivated. The time can be configured in the settings. 
*	ExternalUserClearCache. This queue is used internally on demand to clear user cache in external applications whenever user role changed by administrator in internal application. 
*	ParticipantSyncJob. Runs every 7 days / 168 hours to synchronize CPR data with Valghalla participant data as well as re-validate all assigned tasks for all participants, if they are not valid anymore then the job unassign them automatically and send notifications. The time can be configured in the settings.
* RemovedFromTaskByValidationJob. Runs on demand to remove task when validation engine triggered by another timer job. Timeout and retry period can be configured in the settings.
* RemovedFromTaskJob. Runs on demand when administrator unassign task from participant. Timeout and retry period can be configured in the settings.
* SendGroupMessageJob. Runs on demand when administrator send group message to participants. Timeout and retry period can be configured in the settings.
* TaskCancellationJob. Runs on demand when pariticpant cancel accapted task. Timeout and retry period can be configured in the settings.
* TaskGetInvitationReminderJob. Runs once a day / 24 hours to send task invitation reminders to participants. Time can be configured in the settings.
* TaskGetReminderJob. Runs once a day / 24 hours to send task reminders to participants. Time can be configured in the settings.
*	TaskInvitationJob. This queue is used internally on demand to send task invitations to participants, the job take cares of selecting correct communication platform based on municipality settings (Digital Post, Email or SMS) and write logs to Communication Logs data.
* TaskInvitationRetractedJob. Runs on demand when administrator remove participant from unresponded task and when team responsible remove participant from team that has related tasks. Timeout and retry period can be configured in the settings.
*	TaskRegistrationJob. This queue is used internally on demand to send task registration whenever participants accept tasks, the job take cares of selecting correct communication platform based on municipality settings (Digital Post, Email or SMS) and write logs to Communication Logs data.
* TaskSendInvitationReminderJob. Runs on demand to send communication message for task invitation reminder to participant. Timeout and retry period can be configured in the settings.
* TaskSendReminderJob. Runs on demand to send communication message for task reminder to participant. Timeout and retry period can be configured in the settings.
* UserTokenClearJob. Runs every 4 hours to remove expired user token. Time can be configured in the settings.

The settings for how often a scheduled task will be runned is being set in the appsettings.json for the worker. It's in the hour format so to increase/decrease the days remove 24 from the number. 
