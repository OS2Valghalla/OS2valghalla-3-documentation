Queue and worker
===========

Valghalla is using RabbitMQ as a queue for different events, both the internal and the external application is acting on different queues. 
Then there is also Valghalla worker that is acting on some of the queues.

There are currently five different queues being used in the solution. 

*	ElectionDeactivationJob. Runs every 24 hours to check if election end date is already passed. If the date is passed the election will be deactivated. The time can be configured in the settings. 
*	ExternalUserClearCache. This queue is used internally on demand to clear user cache in external applications whenever user role changed by administrator in internal application. 
*	ParticipantSyncJob. Runs every 24 hours to synchronize CPR data with Valghalla participant data as well as re-validate all assigned tasks for all participants, if they are not valid anymore then the job unassign them automatically and send notifications. The time can be configured in the settings.
*	TaskInvitationJob. This queue is used internally on demand to send task invitations to participants, the job take cares of selecting correct communication platform based on municipality settings (Digital Post, Email or SMS) and write logs to Communication Logs data.
*	TaskRegistrationJob. This queue is used internally on demand to send task registration whenever participants accept tasks, the job take cares of selecting correct communication platform based on municipality settings (Digital Post, Email or SMS) and write logs to Communication Logs data.
