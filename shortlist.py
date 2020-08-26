#!/usr/bin/env python3

import streamlit as st
from PIL import Image

@st.cache
def load_image(player):
    data = Image.open(f'images/{player}.png')
    return data

pos = st.sidebar.selectbox("Select Position",("Overview","Winger","Defensive Midfielder","Centre Back"))

if pos == "Overview":
    st.title("Shortlisting Players for a Champions League Club")

    '''
    This app presents player shortlists for a Champions League club in three roles - Winger, Defensive Midfielder and Centre Back. Use the dropdown menu on left to select the role to view. 
    
    Players have been chosen based primarily on their performance in position-relevant **key attributes** and their **age**. To add context, charts focusing on **style of play** of the player and their team are provided.
    
    Champions League clubs are performing at the highest level and these shortlists aim to highlight players who could not just immediately make an impact, but could continue to do so for a number of years. Given the required standard, only players to have played regular minutes will be considered - with the limit of **at least 1800 minutes** played. Peak age for players is typically in the 24-30 range, with perhaps a slightly older range for defensive players, and players with multiple peak years left are favoured. It is also a benefit to have played in a well performing team - but not necessary - and this is identified by the *Team Rank*, simply the finishing league position of the team.

    It is also important to consdier a player's availability. While only so much can be gathered from the data, if a player is in their middle/late peak years, performing to a high level and making many starts for a top side then it is unlikely they are available.

    Be aware that these are performances for a single season. It is very possible for a player to have an excellent yet unsustainable performance over this timeframe. Ideally, shortlisted players would next be live-scouted to verify the conclusions of the data.
    
    ## Key Attributes
    Unique to each role, key attributes are compared amongst all players relevant for that role. This makes it quick and easy to spot a player who consistently outperforms their peers. All attributes are given **per 90 minutes** played, removing the effect of different total playing times.

    ### Defensive Attributes
    Defending is often more to do with team shape and instructions - something the data struggles to consider. Therefore, while offensive attributes serve as a good way to identify an attacking player's ability, defensive attributes tend to better describe an individual's style rather than skill. For example; are they an active tackler or interceptor? Do they engage in many aerial duels?

    Naturally, however, teams with less of the ball have to do more defending. This is an issue when trying to compare defending styles of players - those from weaker teams do more defending and appear to be more active. To attempt to solve this issue, defensive attributes, namely *tackling* and *interceptions*, are **possession adjusted**.
    
    ## Player and Team Styles
    What does a player or team try to do with/without the ball? The style charts attempt to answer this. Based purely on **quantity**, not quality, a player is compared to all others in the relevant positions to see how often they attempt certain actions. Naturally, a player is embedded within a team with its own style and will be influenced by this. Hence, team style is provided for additional context.
    '''

elif pos == "Winger":
    
    st.title("Winger Shortlist")
    '''
    The winger role can take on a number of forms, for example - skilled 1-on-1, wide playmaker, crosser or inside forward. Each of these requires a slightly different skill set. When identifying wingers, players are initially shortlisted by a competency across many skills before focusing on a specific skill set.

    Players in the *Midfielder* and *Forward* positions up to the age of 30 are considered.

    ## Player ID: 119718

    Perhaps fitting the *inside forward* role, this player has been a real threat in front of goal - taking many shots, often from good positions, and converting. It is clear they also excel at dribbling, doing it often and with great success. While their creation for teammates is not quite on the same level, it is still good and is complimented by competent crossing. However, as can be expected of a player who shoots and dribbles often, they often conceed possession.

    Having made 27 starts for the team ranked 3rd, this is player used to playing at a high level. However, this team is not particularly passing focused and indeed this player does not pass often when compared to others - may not be naturally suited to a passing-heavy team.

    '''

    st.image(load_image('wing1'), use_column_width=True)
    
    '''
    ## Player ID: 108438

    Goal scoring is this player's primary attribute, taking the most shots and scoring the most goals of any player considered. While the xG number suggests this player has had many good opportunities to score, note that the player has overperformed in number of goals - something that may not be sustainable. Outside of shooting, this player is a good, if not great, creator and crosser as well as retaining possession well. Clearly, however, this is not a dribbler, having middling attempts and success. Indeed, this is also not a player with a passing heavy game.

    Having made 28 starts in 30 games played, this has been an important player for their side. Ranked 11th, this team is mid-table and this player therefore likely lacks some high-level experience.
    '''
    
    st.image(load_image('wing2'), use_column_width=True)
    
    '''
    ## Player ID: 156689
    
    With great key passing and penalty area entries, this is a player who excels at creating, supported by excellent crossing and dribbling. A player who could fulfill the *wide playermaker* role. However, clearly ambitious in making chances, there is an incredibly large amount of possession losses. Additionally, this player likes to take many shots but mostly from poor positions.

    At just 24 years old, this player has been a guaranteed starter for their team. Yet, this was the lowest ranked team in the competition so high level experience is absent. Despite the team deficiencies, they have produced high amounts across almost all styles - making it likely they were the focal point of the team.
    '''
    
    st.image(load_image('wing3'), use_column_width=True)

elif pos == "Defensive Midfielder":
    st.title("Defensive Midfielder Shortlist")
    '''
    Defensive midfield is a diverse position that involves a mix of defensive duties, ball retention and ball progression. Two main roles were considered for this shortlist: 
    - *disrupter*: focus on defensive duties
    - *deep lying progressor/playmaker*: focus on moving the ball up the field with some underlying defensive ability

    Players in the *Midfielder* position up to the age of 30 were considered.

    All of the players on this list are young (25 or 24) and would therefore present good long-term options.

    ## Player ID: 192364

    Excellent anticipation demonstrated by interceptions supported by active tackling and a competency in aerial duels - this is a player who could be effective at gaining possession. Once in possession, this is a very safe passer, looking to retain rather than progress and could work well alongside a more creative midfielder - where this player is clearly lacking.

    Having made 31 starts and with their own style much more active than their team's, this is someone who can play a central role in a team. And at the age of just 25, there is still room to improve.
    '''
    st.image(load_image('dm1'), use_column_width=True)

    '''
    ## Player ID: 89335

    Very active tackling and dominance in the air indicates a player who could again be very effective at disrupting opposition play. Once in possession however, this is a player who tends to take more risks trying to progress the ball - shown by a good level of final third entries but poor pass success % and possession losses. This is also a player who fouls a lot, so discipline could be an issue.

    Making 29 starts in the 3rd ranked team shows this player can be trusted at a high level and is just 25.
    '''
    
    st.image(load_image('dm2'), use_column_width=True)
    
    '''
    ## Player ID: 182539

    While this player is a proactive tackler and ball-winner, their excellence comes in the form of ball progression into the final third and an unrivaled level of dribbling. Clearly comfortable on the ball, this player also creates a good amount of shooting opportunitie for teammates. While a somewhat effective ball-winner, they lack the aerial prowess to be the rock of a midfield. Additonally, as comes with a progressive style, this player often turns possession over.

    With 24 starts in 33 games played, this player established themselves as an important squad member - with the styles demonstrating how much of a focal point they were. While lacking some high-level experience having played at the 15th ranked team, the player is only 24 and these already impressive numbers will have ample time to further improve.
    '''
    
    st.image(load_image('dm3'), use_column_width=True)
    
elif pos == 'Centre Back':
    st.title("Centre Back Shortlist")
    '''
    Given the stylistic nature of defensive metrics, it is harder to definitively identify good centre backs. The approach here is to get a baseline ability judged off tackle success and aerial prowess, then further classify style by examining other attributes. Champions League clubs are often the dominant team in games and it has become important for centre backs to be comfortable on the ball - something that has been considered. 

    Players in the *Centre Back* position up to the age of 32 are included.

    ## Player ID: 88580

    Dominant aerially and very successful when tackling, this player has an excellent defensive foundation. While not the most active tackler, the player engages in a  high amount of intercepting - in-line with team style. Additionally, they are very safe on the ball, playing many conservative passes and, with a team style heavily based in passing, are likely comfortable on the ball. However, this is not a centre back for quickly progressing play up the field.

    At just 26 this player has outstanding attributes and plays in a top side which finished 2nd. However, they haven't been a guaranteed starter with 24 starts in 33 games played.
    '''
    
    st.image(load_image('cb1'), use_column_width=True)
    
    '''
    ## Player ID: 146941

    Fantastic in the air but only middling success with tackles, although is not a particularly active tackler anyway. Also not a high volume interceptor, but this matches team style. This player stands out because of their progression. While possession losses and pass success % clearly suffer in comparison to the other two options on this list, they are still surprisingly high given the volume of long balls the player attempts. This suggests an accurate long passer, a skill that can undoubtedly aid a team in progressing quickly up the pitch.

    Having started all 33 games played for the 6th ranked team, this is a player who has already be trusted at a high (if not top) level. At 26, the player should also have many peak years ahead of them.
    '''
    
    st.image(load_image('cb2'), use_column_width=True)
    
    '''
    ## Player ID: 90152

    Completely dominant in the air but not the most accomplished tackler, tending to avoid them. This is another player who looks very sure in possession -  retaining it well with simple passes and giving away very few fouls. Looks like an all-round incredibly solid defensive option.

    An almost guaranteed starter when playing (23 starts in 26 games played) for the top ranked side indicate this is a player comfortable at the highest level, although that may mean they are unavailable.
    '''
    
    st.image(load_image('cb3'), use_column_width=True)