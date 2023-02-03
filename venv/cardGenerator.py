import numpy as np
import os, sys
from PIL import Image, ImageFont, ImageDraw
import textwrap
import csv


if __name__==    "__main__":

    #directories
    base_dir='C:\\Users\\kuusv\\Desktop\\Tavern V2'
    template_dir=base_dir+'\\templates'
    current_dir=os.getcwd()

    #import database
    cards=np.loadtxt(base_dir+'\\databases\\taverncards.csv',delimiter=",", dtype=str, skiprows=2)

    #base dimensions (of playing card. Standard is 64mm x 89mm. Tabletopia is 10 px per mm)
    cardwidth=635
    cardheight=888
    margin=[40, 30]
    iconSize=[100, 100]

    #open template
    HeroTemplate = Image.open("{}\\herotemplate.png".format(template_dir))
    ActionTemplate=Image.open("{}\\actiontemplate.png".format(template_dir))
    ModuleTemplate=Image.open("{}\\moduletemplate.png".format(template_dir))
    Questtemplate=Image.open("{}\\questtemplate.png".format(template_dir))

    #open icons
        #races
    human=Image.open("{}\\images\\icons\\human.png".format(base_dir))
    dwarf=Image.open("{}\\images\\icons\\dwarf.png".format(base_dir))
    goblin=Image.open("{}\\images\\icons\\goblin.png".format(base_dir))
    orc=Image.open("{}\\images\\icons\\orc.png".format(base_dir))
    elf=Image.open("{}\\images\\icons\\elf.png".format(base_dir))

    #classes
    warrior=Image.open("{}\\images\\icons\\warrior.png".format(base_dir))
    mage=Image.open("{}\\images\\icons\\mage.png".format(base_dir))
    troubadour=Image.open("{}\\images\\icons\\troubadour.png".format(base_dir))
    bandit=Image.open("{}\\images\\icons\\bandit.png".format(base_dir))
    champion=Image.open("{}\\images\\icons\\champion.png".format(base_dir))
    cultist=Image.open("{}\\images\\icons\\cultist.png".format(base_dir))
    priest=Image.open("{}\\images\\icons\\priest.png".format(base_dir))
    any=Image.open("{}\\images\\icons\\any.png".format(base_dir))


    #fonts
    titleSize=90; raceclassTextSize=45; heroDescriptionTextSize=40;
    font_name = ImageFont.truetype(r'{}\\fonts\\kings.ttf'.format(base_dir), titleSize)
    font_raceclass = ImageFont.truetype(r'{}\\fonts\\arial.ttf'.format(base_dir), raceclassTextSize)
    font_herodescription = ImageFont.truetype(r'{}\\fonts\\blackjack.otf'.format(base_dir), heroDescriptionTextSize)

    #cardLocations
    titleCoords=[margin[0], margin[1]]
    raceCoords=(margin[0], 270)
    classCoords=(margin[0]+200, raceCoords[1])
    descriptionCoords=(margin[0], 450)
    abilityCoords=(margin[0], 420)

    rage1Coords=(margin[0], abilityCoords[1]+5*heroDescriptionTextSize)
    rage2Coords = (margin[0], abilityCoords[1]+7*heroDescriptionTextSize)

    #textbox sizes
    descriptionWidth=34
    nameWidth=20

    #mysterious shift factors
    shiftFactor=0.9

    #determine card type. Hero, Quest, Module
    for card in (cards[:, 0]):
        card=int(card)-1
        for i in range(int(cards[card, 6])):
            #ACTION
            if cards[card, 2]=='Action':
                cardPNG=ActionTemplate.copy()
                # Name
                I1 = ImageDraw.Draw(cardPNG)
                text = textwrap.wrap("{}".format(cards[card, 1]), width=int(nameWidth))
                for nt in range(len(text)):
                    I1.text(np.add(titleCoords, [0, nt * titleSize*shiftFactor]), text[nt], fill=(10, 10, 10), font=font_name)


                # Description
                text = textwrap.wrap("{}".format(cards[card, 4]), width=int(36))
                for nt in range(len(text)):
                    I1.text(np.add(descriptionCoords,[0, nt*heroDescriptionTextSize]), text[nt], fill=(10, 10, 10), font=font_herodescription)


                cardPNG.save("{}\\Results\\card{}_{}.png".format(base_dir, card + 1, i + 1))

            #QUEST
            if cards[card, 2]=='Quest':
                cardPNG = Questtemplate.copy()
                # Name
                I1 = ImageDraw.Draw(cardPNG)
                text = textwrap.wrap("{}".format(cards[card, 1]), width=int(nameWidth))
                for nt in range(len(text)):
                    I1.text(np.add(titleCoords, [0, nt * titleSize*shiftFactor]), text[nt], fill=(10, 10, 10), font=font_name)

                #Requirement 1
                if cards[card, 8]=='any':
                    I1.text(raceCoords, 'ANY', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(any, (raceCoords[0], raceCoords[1]+raceclassTextSize), any)  # add icon
                    raceLen = font_raceclass.getsize('ANY')[0]
                if cards[card, 8]=='warrior':
                    I1.text(raceCoords, 'WARRIOR', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(warrior, (raceCoords[0], raceCoords[1]+raceclassTextSize), warrior)  # add icon
                    raceLen = font_raceclass.getsize('WARRIOR')[0]
                if cards[card, 8]=='bandit':
                    I1.text(raceCoords, 'BANDIT', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(bandit, (raceCoords[0], raceCoords[1]+raceclassTextSize), bandit)  # add icon
                    raceLen = font_raceclass.getsize('BANDIT')[0]
                if cards[card, 8]=='priest':
                    I1.text(raceCoords, 'PRIEST', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(priest, (raceCoords[0], raceCoords[1]+raceclassTextSize), priest)  # add icon
                    raceLen = font_raceclass.getsize('PRIEST')[0]
                if cards[card, 8]=='troubadour':
                    I1.text(raceCoords, 'MINSTREL', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(troubadour, (raceCoords[0], raceCoords[1]+raceclassTextSize), troubadour)  # add icon
                    raceLen = font_raceclass.getsize('MINSTREL')[0]
                if cards[card, 8]=='mage':
                    I1.text(raceCoords, 'MAGE', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(mage, (raceCoords[0], raceCoords[1]+raceclassTextSize), mage)  # add icon
                    raceLen = font_raceclass.getsize('MAGE')[0]
                if cards[card, 8]=='champion':
                    I1.text(raceCoords, 'CHAMPION', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(champion, (raceCoords[0], raceCoords[1]+raceclassTextSize), champion)  # add icon
                    raceLen = font_raceclass.getsize('CHAMPION')[0]
                if cards[card, 8]=='cultist':
                    I1.text(raceCoords, 'CULTIST', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(cultist, (raceCoords[0], raceCoords[1]+raceclassTextSize), cultist)  # add icon
                    raceLen = font_raceclass.getsize('CULTIST')[0]


                # Requirement 2
                if cards[card, 9]=='any':
                    I1.text([raceCoords[0]+raceLen, raceCoords[1]], ', ANY', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(any, (raceCoords[0]+iconSize[0]+margin[0], raceCoords[1]+raceclassTextSize), any)  # add icon
                if cards[card, 9]=='warrior':
                    I1.text([raceCoords[0]+raceLen, raceCoords[1]], ', WARRIOR', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(warrior, (raceCoords[0]+iconSize[0]+margin[0], raceCoords[1]+raceclassTextSize), warrior)  # add icon
                if cards[card, 9]=='bandit':
                    I1.text([raceCoords[0]+raceLen, raceCoords[1]], ', BANDIT', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(bandit, (raceCoords[0]+iconSize[0]+margin[0], raceCoords[1]+raceclassTextSize), bandit)  # add icon
                if cards[card, 9]=='priest':
                    I1.text([raceCoords[0]+raceLen, raceCoords[1]], ', PRIEST', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(priest, (raceCoords[0]+iconSize[0]+margin[0], raceCoords[1]+raceclassTextSize), priest)  # add icon
                if cards[card, 9]=='troubadour':
                    I1.text([raceCoords[0]+raceLen, raceCoords[1]], ', MINSTREL', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(troubadour, (raceCoords[0]+iconSize[0]+margin[0], raceCoords[1]+raceclassTextSize), troubadour)  # add icon
                if cards[card, 9]=='mage':
                    I1.text([raceCoords[0]+raceLen, raceCoords[1]], ', MAGE', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(mage, (raceCoords[0]+iconSize[0]+margin[0], raceCoords[1]+raceclassTextSize), mage)  # add icon
                if cards[card, 9]=='champion':
                    I1.text([raceCoords[0]+raceLen, raceCoords[1]], ', CHAMPION', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(champion, (raceCoords[0]+iconSize[0]+margin[0], raceCoords[1]+raceclassTextSize), champion)  # add icon
                if cards[card, 9]=='cultist':
                    I1.text([raceCoords[0]+raceLen, raceCoords[1]], ', CULTIST', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(cultist, (raceCoords[0]+iconSize[0]+margin[0], raceCoords[1]+raceclassTextSize), cultist)  # add icon

                # Race of Questgiver
                if cards[card, 10] == 'human':
                    I1.text(descriptionCoords, 'Questgiver: HUMAN  ', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(human, (descriptionCoords[0]+font_raceclass.getsize('Questgiver: HUMAN ')[0], descriptionCoords[1]-int(iconSize[1]*0.25)), human)  # add icon
                if cards[card, 10] == 'dwarf':
                    I1.text(descriptionCoords, 'Questgiver: DWARF  ', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(dwarf, (descriptionCoords[0]+font_raceclass.getsize('Questgiver: DWARF ')[0], descriptionCoords[1]-int(iconSize[1]*0.25)), dwarf)  # add icon
                if cards[card, 10] == 'goblin':
                    I1.text(descriptionCoords, 'Questgiver: GOBLIN ', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(goblin, (descriptionCoords[0]+font_raceclass.getsize('Questgiver: GOBLIN ')[0], descriptionCoords[1]-int(iconSize[1]*0.25)), goblin)  # add icon
                if cards[card, 10] == 'elf':
                    I1.text(descriptionCoords, 'Questgiver: ELF ', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(elf, (descriptionCoords[0]+font_raceclass.getsize('Questgiver: ELF ')[0], descriptionCoords[1]-int(iconSize[1]*0.25)), elf)  # add icon
                if cards[card, 10] == 'orc':
                    I1.text(descriptionCoords, 'Questgiver: ORC ', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(orc, (descriptionCoords[0]+font_raceclass.getsize('Questgiver: ORC ')[0], descriptionCoords[1]-int(iconSize[1]*0.25)), orc)  # add icon

                #Numerical Reward
                I1.text(rage1Coords, 'FAME REWARD: {}'.format(cards[card, 3]), fill=(10, 10, 10), font=font_raceclass)

                #Ability Reward
                if cards[card, 4]!='NULL':
                    I1.text(rage2Coords, 'ABILITY REWARD:'.format(cards[card, 4]), fill=(10, 10, 10),
                            font=font_raceclass)
                    I1.text(np.add(rage2Coords, [0, raceclassTextSize]), '{}'.format(cards[card, 4]), fill=(10, 10, 10),
                            font=font_raceclass)


                cardPNG.save("{}\\Results\\card{}_{}.png".format(base_dir, card + 1, i + 1))


            #MODULE
            if cards[card, 2]=='Expansion':
                cardPNG = ModuleTemplate.copy()
                # Name
                I1 = ImageDraw.Draw(cardPNG)
                text = textwrap.wrap("{}".format(cards[card, 1]), width=int(nameWidth))
                for nt in range(len(text)):
                    I1.text(np.add(titleCoords, [0, nt * titleSize*shiftFactor]), text[nt], fill=(10, 10, 10), font=font_name)

                # Description
                text = textwrap.wrap("{}".format(cards[card, 4]), width=int(descriptionWidth))
                for nt in range(len(text)):
                    I1.text(np.add(descriptionCoords,[0, nt*heroDescriptionTextSize]), text[nt], fill=(10, 10, 10), font=font_herodescription)

                cardPNG.save("{}\\Results\\card{}_{}.png".format(base_dir, card + 1, i + 1))

            #HERO
            if cards[card, 2]=='Hero':
                cardPNG = HeroTemplate.copy()
                #Name
                I1 = ImageDraw.Draw(cardPNG)
                text = textwrap.wrap("{}".format(cards[card, 1]), width=int(nameWidth))
                for nt in range(len(text)):
                    I1.text(np.add(titleCoords,[0, nt*titleSize*shiftFactor]), text[nt], fill=(10, 10, 10), font=font_name)


                if cards[card, 8]=='human':
                    I1.text(raceCoords, 'HUMAN', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(human, (raceCoords[0], raceCoords[1]+raceclassTextSize), human)  # add icon
                    raceLen=font_raceclass.getsize('HUMAN ')


                if cards[card, 8]=='dwarf':
                    I1.text(raceCoords, 'DWARF', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(dwarf, (raceCoords[0], raceCoords[1]+raceclassTextSize), dwarf)  # add icon
                    raceLen=font_raceclass.getsize('DWARF ')

                if cards[card, 8]=='goblin':
                    I1.text(raceCoords, 'GOBLIN', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(goblin, (raceCoords[0], raceCoords[1]+raceclassTextSize), goblin)  # add icon
                    raceLen=font_raceclass.getsize('GOBLIN ')

                if cards[card, 8]=='orc':
                    I1.text(raceCoords, 'ORC', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(orc, (raceCoords[0], raceCoords[1]+raceclassTextSize), orc)  # add icon
                    raceLen=font_raceclass.getsize('ORC ')

                if cards[card, 8]=='elf':
                    I1.text(raceCoords, 'ELF', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(elf, (raceCoords[0], raceCoords[1]+raceclassTextSize), elf)  # add icon
                    raceLen=font_raceclass.getsize('ELF ')

                ######


                #Class
                if cards[card, 9]=='warrior':
                    I1.text([raceCoords[0]+raceLen[0], raceCoords[1]], 'WARRIOR', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(warrior, (classCoords[0], classCoords[1]+raceclassTextSize), warrior)  # add icon
                if cards[card, 9]=='bandit':
                    I1.text([raceCoords[0]+raceLen[0], raceCoords[1]], 'BANDIT', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(bandit, (classCoords[0], classCoords[1]+raceclassTextSize), bandit)  # add icon
                if cards[card, 9]=='priest':
                    I1.text([raceCoords[0]+raceLen[0], raceCoords[1]], 'PRIEST', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(priest, (classCoords[0], classCoords[1]+raceclassTextSize), priest)  # add icon
                if cards[card, 9]=='troubadour':
                    I1.text([raceCoords[0]+raceLen[0], raceCoords[1]], 'MINSTREL', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(troubadour, (classCoords[0], classCoords[1]+raceclassTextSize), troubadour)  # add icon
                if cards[card, 9]=='mage':
                    I1.text([raceCoords[0]+raceLen[0], raceCoords[1]], 'MAGE', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(mage, (classCoords[0], classCoords[1]+raceclassTextSize), mage)  # add icon
                if cards[card, 9]=='champion':
                    I1.text([raceCoords[0]+raceLen[0], raceCoords[1]], 'CHAMPION', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(champion, (classCoords[0], classCoords[1]+raceclassTextSize), champion)  # add icon
                if cards[card, 9]=='cultist':
                    I1.text([raceCoords[0]+raceLen[0], raceCoords[1]], 'CULTIST', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(cultist, (classCoords[0], classCoords[1]+raceclassTextSize), cultist)  # add icon

                # Ability

                I1.text(abilityCoords, 'ABILITY:', fill=(10, 10, 10), font=font_herodescription)
                text = textwrap.wrap("{}".format(cards[card, 3]), width=int(descriptionWidth))
                for na in range(len(text)):
                    I1.text(np.add(abilityCoords,[0, (na+1)*heroDescriptionTextSize]), text[na], fill=(10, 10, 10), font=font_herodescription)

                #Rage 1
                I1.text(rage1Coords, 'RAGE 1 EFFECT: ', fill=(10, 10, 10), font=font_herodescription)
                text = textwrap.wrap("{}".format(cards[card, 4]), width=int(descriptionWidth))
                for nr in range(len(text)):
                    I1.text(np.add(rage1Coords,[0, (nr+1)*heroDescriptionTextSize]), text[nr], fill=(10, 10, 10), font=font_herodescription)

                # Rage 2
                I1.text(rage2Coords, 'RAGE 2 EFFECT: ', fill=(10, 10, 10), font=font_herodescription)
                text = textwrap.wrap("{}".format(cards[card, 5]), width=int(descriptionWidth))
                for nr1 in range(len(text)):
                    I1.text(np.add(rage2Coords, [0, (nr1+1) * heroDescriptionTextSize]), text[nr1], fill=(10, 10, 10), font=font_herodescription)


                #Tantrum
               # print(cards[card, 4])
                #print(cards[card, 5])



                #print(cards[card, 6])

                cardPNG.save("{}\\Results\\card{}_{}.png".format(base_dir, card+1, i + 1))
                #if card==1:
                    #sys.exit()

    #OLD CODE################################################################################################################
    ################################################################################################################################
    sys.exit()


    herotemplate=Image.open("{}\\herotemplate.png".format(base_dir))


    #alignments
    #good = Image.open("{}\\images\\icons\\good.png".format(path))
    #evil = Image.open("{}\\images\\icons\\evil.png".format(path))

    classrace_im=[warrior, bandit, priest, troubadour, mage,
                  champion, cultist, any, human, dwarf, goblin, orc, elf, elemental, good, evil]


    nHeroes = len(np.transpose(herodata)[0])
    for i in range(nHeroes):
        characters=len(herodata[i][1])
        if characters>=15:
            nameW=int(width*0.1)-int(((characters-12)**1.1)*0.6)
        else:
            nameW=int(width*0.1)
        font_name = ImageFont.truetype(r'{}}\\fonts\\arial.ttf'.format(base_dir), nameW)
        #font_t = ImageFont.truetype(r'C:\\Users\\kuusv\\Desktop\\TavernGame\\Jobs\\pythonCards\\arial.ttf', int(width*0.05))
        #font_d = ImageFont.truetype(r'C:\\Users\\kuusv\\Desktop\\TavernGame\\Jobs\\pythonCards\\arial.ttf', int(width*0.25))

        # Draw title
        templateCopy = herotemplate.copy()
        I1 = ImageDraw.Draw(templateCopy)
        I1.text((int(width*0.1), int(height*0.1)), "{}".format(herodata[i][1]), fill=(10, 10, 10), font=font_name)

        # Draw Drink Requirement
        I1.text((int(width*0.4), int(height*0.75)), "{}".format(herodata[i][9]), fill=(10, 10, 10), font=font_d)

        #Draw alignment
        aligncoords=[int(width*0.8), int(height*0.25)]
        if int(herodata[i][11])==0:
            templateCopy.paste(good.convert("RGBA"), aligncoords, good.convert("RGBA"))  # add icon
        elif int(herodata[i][11])==1:
            templateCopy.paste(evil.convert("RGBA"), aligncoords, evil.convert("RGBA"))  # add icon


        # Draw Race
        racecoords=[int(width*0.1), int(height*0.25)]

        if herodata[i][2]=='human':
            templateCopy.paste(classrace_im[8].convert("RGBA"), racecoords, classrace_im[8].convert("RGBA"))  # add icon
        elif herodata[i][2]=='dwarf':
            templateCopy.paste(classrace_im[9].convert("RGBA"), racecoords, classrace_im[9].convert("RGBA"))  # add icon
        elif herodata[i][2] == 'goblin':
            templateCopy.paste(classrace_im[10].convert("RGBA"), racecoords, classrace_im[10].convert("RGBA"))  # add icon

        elif herodata[i][2] == 'orc':
            templateCopy.paste(classrace_im[11].convert("RGBA"), racecoords, classrace_im[11].convert("RGBA"))  # add icon

        elif herodata[i][2] == 'elf':
            templateCopy.paste(classrace_im[12].convert("RGBA"), racecoords, classrace_im[12].convert("RGBA"))  # add icon

        elif herodata[i][2] == 'elemental':
            templateCopy.paste(classrace_im[13].convert("RGBA"), racecoords, classrace_im[13].convert("RGBA"))  # add icon

        # Draw Class
        classcoords=[int(width*0.1), int(height*0.4)]
        if herodata[i][3]=='warrior':
            templateCopy.paste(classrace_im[0].convert("RGBA"), classcoords, classrace_im[0].convert("RGBA"))  # add icon
        if herodata[i][3]=='bandit':
            templateCopy.paste(classrace_im[1].convert("RGBA"), classcoords, classrace_im[1].convert("RGBA"))  # add icon
        if herodata[i][3]=='priest':
            templateCopy.paste(classrace_im[2].convert("RGBA"), classcoords, classrace_im[2].convert("RGBA"))  # add icon
        if herodata[i][3]=='troubadour':
            templateCopy.paste(classrace_im[3].convert("RGBA"), classcoords, classrace_im[3].convert("RGBA"))  # add icon
        if herodata[i][3]=='mage':
            templateCopy.paste(classrace_im[4].convert("RGBA"), classcoords, classrace_im[4].convert("RGBA"))  # add icon
        if herodata[i][3]=='champion':
            templateCopy.paste(classrace_im[5].convert("RGBA"), classcoords, classrace_im[5].convert("RGBA"))  # add icon
        if herodata[i][3]=='cultist':
            templateCopy.paste(classrace_im[6].convert("RGBA"), classcoords, classrace_im[6].convert("RGBA"))  # add icon


        #Add Tantrum

        text=textwrap.wrap(herodata[i][10], width=30)
        I1.text((int(width*0.1), int(height*0.5)), "Tantrum:", fill=(10, 10, 10), font=font_t)
        for nt in range(len(text)):
            textheight=30
            I1.text((int(width*0.1), int(height*0.55)+nt*textheight), "{}".format(text[nt]), fill=(10, 10, 10), font=font_t)


        templateCopy.save("{}\\Results\\Heroes\\Hero{}.png".format(path, i + 1))



