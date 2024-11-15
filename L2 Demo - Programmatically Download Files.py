#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import os


# In[2]:


# Make directory if it doesn't already exist
folder_name = 'ebert_reviews_2017'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)


# In[3]:


ebert_review_urls = ['https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9900_1-the-wizard-of-oz-1939-film/1-the-wizard-of-oz-1939-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9901_2-citizen-kane/2-citizen-kane.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9901_3-the-third-man/3-the-third-man.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/SeptemberBumblebee/59ad9901_3-the-third-man/3-the-third-man.txt']


# In[4]:


for url in ebert_review_urls:
    #Create an HTTP GET request for Ebert reviews
    response = requests.get(url)
    #Raise an exception if we made a request resulting in an error
    response.raise_for_status()
    #Define the filepath by incorporating the folder_name and the last part of the url
    file_path = os.path.join(folder_name, url.split('/')[-1])
    print(file_path)
    #Writing in binary mode
    with open(file_path, mode = 'wb') as file:
        file.write(response.content)


# In[ ]:


os.listdir(folder_name)


# In[ ]:


# %load ebert_reviews_2017/3-the-third-man.txt
The Third Man (1949)
http://www.rogerebert.com/reviews/great-movie-the-third-man-1949
Has there ever been a film where the music more perfectly suited the action than in Carol Reed's "The Third Man"? The score was performed on a zither by Anton Karas, who was playing in a Vienna beerhouse one night when Reed heard him. The sound is jaunty but without joy, like whistling in the dark. It sets the tone; the action begins like an undergraduate lark and then reveals vicious undertones.

The story begins with a spoken prologue ("I never knew the old Vienna, before the war. . ."). The shattered postwar city has been divided into French, American, British and Russian zones, each with its own cadre of suspicious officials. Into this sinkhole of intrigue falls an American innocent: Holly Martins (Joseph Cotton), alcoholic author of pulp Westerns. He has come at the invitation of his college chum Harry Lime. But Lime is being buried when Martins arrives in Vienna.

How did Lime die? That question is the engine that drives the plot, as Martins plunges into the murk that Lime left behind. Calloway (Trevor Howard), the British officer in charge, bluntly says Lime was an evil man, and advises Holly to take the next train home. But Harry had a girl named Anna (Alida Valli), who Holly sees at Lime's grave, and perhaps she has some answers. Certainly Holly has fallen in love with her, although his trusting Yankee heart is no match for her defenses.

"The Third Man" (1949) was made by men who knew the devastation of Europe at first hand. Carol Reed worked for the British Army's wartime documentary unit, and the screenplay was by Graham Greene, who not only wrote about spies but occasionally acted as one. Reed fought with David O. Selznick, his American producer, over every detail of the movie; Selznick wanted to shoot on sets, use an upbeat score and cast Noel Coward as Harry Lime. His film would have been forgotten in a week. Reed defied convention by shooting entirely on location in Vienna, where mountains of rubble stood next to gaping bomb craters, and the ruins of empire supported a desperate black market economy. And he insisted on Karas' zither music ("The Third Man Theme" was one of 1950's biggest hits).

Reed and his Academy Award-winning cinematographer, Robert Krasker, also devised a reckless, unforgettable visual style. More shots, I suspect, are tilted than are held straight; they suggest a world out of joint. There are fantastic oblique angles. Wide-angle lenses distort faces and locations. And the bizarre lighting makes the city into an expressionist nightmare. (During a stakeout for Lime, a little balloon man wanders onto the scene, and his shadow is a monster three stories high). Vienna in "The Third Man" is a more particular and unmistakable *place* than almost any other location in the history of the movies; the action fits the city like a hand slipping on a glove.

Then there are the faces: Joseph Cotton's open, naive face contrasts with the "friends" of Harry Lime: the corrupt "Baron" Kurtz (Ernst Deutsch); the shifty Dr. Winkel (Erich Ponto), the ratlike Popescu (Siegfried Breuer). Even a little boy with a rubber ball looks like a wizened imp. The only trusting faces are those of innocents like the hall porter (Paul Hoerbiger) who tells Holly, "There was another man . . . a third man. . ." and the beefy Sgt. Paine (Bernard Lee), Calloway's aide, who levels the drunken Holly with a shot to the chin and then apologizes. Even the resident exiles are corrupt; Crabbin (Wilfrid Hyde-White), the head of the discussion group, chatters about culture while smoothly maneuvering his mistress out of sight through doors and up stairs.

As for Harry Lime: He allows Orson Welles to make the most famous entrance in the history of the movies, and one of the most famous speeches. By the time Lime finally appears we have almost forgotten Welles is even *in* the movie. The sequence is unforgettable: the meow of the cat in the doorway, the big shoes, the defiant challenge by Holly, the light in the window, and then the shot, pushing in, on Lime's face, enigmatic and teasing, as if two college chums had been caught playing a naughty prank.

The famous speech comes during an uneasy ride on a giant Ferris wheel; at one point, Lime slides open the door of the car they are riding in, and Holly uneasily wraps an arm around a post. Harry tries to justify himself: "You know what the fellow said: In Italy for 30 years under the Borgias they had warfare, terror, murder and bloodshed, but they produced Michelangelo, Leonardo da Vinci and the Renaissance. In Switzerland they had brotherly love--they had 500 years of democracy and peace, and what did that produce? The cuckoo clock." (Greene says this speech was written by Welles.)

The emotional heart of the movie is Holly's infatuation with Anna, who will love Harry and be grateful to him no matter what she learns. The scenes between Holly and Anna are enriched by tiny details, as when they visit Harry's apartment and she opens a drawer without looking--because she already knows what will be inside. Or the way she sometimes slips and calls Holly "Harry." Everyone in the movie has trouble with names. Holly calls Calloway "Callahan," and Dr. Winkle insists on "VINK-ell!" And the name on Harry Lime's tombstone is wrong, too.

The chase sequence in "The Third Man" is another joining of the right action with the right location. Harry escapes into the sewer system like a cornered rat, and Reed edits the pursuit into long, echoing, empty sewer vistas, and closeups of Lime's sweaty face, his eyes darting for a way out. Presumably there would be no lights in the Vienna sewers, but there are strong light sources just out of sight behind every corner, throwing elongated shadows, backlighting Harry and his pursuers.

The final scene in "The Third Man" is a long, elegiac sigh. It almost did not exist. Selznick and Greene originally wanted a happy ending. (Greene originally wrote, ". . . her hand was through his arm"). Reed convinced Greene he was wrong. The movie ends as it begins, in a cemetery, and then Calloway gives Holly a ride back to town. They pass Anna walking on the roadside. Holly asks to be let out of the jeep. He stands under a tree, waiting for her. She walks toward him, past him, and then out of frame, never looking. After a long pause, Holly lights a cigarette and wearily throws away the match. Joseph Cotten recalled later that he thought the scene would end sooner. But Reed kept the camera running, making it an unusually long shot, and absolutely perfect.

"The Third Man" reflects the optimism of Americans and the bone-weariness of Europe after the war. It's a story about grownups and children: Adults like Calloway, who has seen at first hand the results of Lime's crimes, and children like the trusting Holly, who believes in the simplified good and evil of his Western novels.

"The Third Man" is like the exhausted aftermath of "Casablanca." Both have heroes who are American exiles, awash in a world of treachery and black market intrigue. Both heroes love a woman battered by the war. But "Casablanca" is bathed in the hope of victory, while "The Third Man" already reflects the Cold War years of paranoia, betrayal and the Bomb. The hero doesn't get the girl in either movie--but in "Casablanca," Ilsa stays with the resistance leader to help in his fight, while in "The Third Man" Anna remains loyal to a rat. Yet Harry Lime saved Anna, a displaced person who faced certain death. Holly will never understand what Anna did to survive the war, and Anna has absolutely no desire to tell him.

get_ipython().run_line_magic('pinfo', 'knowledge')


# In[ ]:





# In[ ]:





# In[ ]:




