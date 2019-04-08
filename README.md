Service Instance Action
This sample is a prototype to stop instances based on TAG Values.
This strategy allow us to implement one very useful interaction for tagging strategy - Automation.

For tagging automation strategy, we can assume non production workloads can be labeled to not be active out of work hours.
First we must implement and apply the tagging value that will be observed as the main parameters for this script.
We can use the best fit scheduler of your choice: crontab, jenkings etc.. 
Other aspect to reinforce this ca be the tagging default - this feature allows apply by default tagkeys and values. 
Example: non-production - dev compartment: can have the tagging default (tag key and value).

Scenario: 
Choice: Type: Free formTag
        TagKey: ENVIRONMENT
        TagValue: DEV
        
OBS.: Important remember organization is a MUST be emphasis with uppercase,  start planning first - at least with minimum logical organization strategy. "Compartments and TAGs"

Have fun and welcome 
 
