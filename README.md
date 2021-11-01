`App`
An app the user has created in our platform. Includes metadata about the app such
as name and description.
`Plan`
Plans to which a user can subscribe their app. Plans are billed on a monthly basis.
Price can be 0.
Your app should have three plans: Free ($0), Standard ($10), Pro ($25).
`Subscription`
Subscription tracks what plan is associated with an app. For record keeping
subscriptions are never deleted, their active attribute is set to False.
