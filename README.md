This is unfinished and doesn't warrant a second look. Team members decided they don't want to continue and I had to switch from backend parts and AI integration to doing basic frontend bolierplate and while I made some progress it's clear that I'm not going to finish this in time for submission. I'll continue building in slow mode, I still like the idea. And want to train drones, looking into costs and potential sponsors.

Ideally I'd water water bottles delivered by actual automated drones but I have no time to train them and no budget to buy hardware so I'm focusing on scaffloding for now.

![image](https://github.com/user-attachments/assets/e3a0dcbb-2e38-47fd-ab4e-a6df46ed3025)

Main control happens in Telegram with a bot. Live location sharing works reliably there and frontend person left the team last-minute so it seems to make most sense. Bot integrates Ora for human-like responses and (in future) some message parsing so that drones can actually be controlled to some extent.

On-chain part is very basic and consists of staking some initial stake, minting proof of participation (on water delivery) and proof of proper recycling. Most of the stake is returned if proof of recycling was minted (also other privileges will be provided for responsible users).
