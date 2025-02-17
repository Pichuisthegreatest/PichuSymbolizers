import tkinter as tk
from tkinter import Button, Label, ttk, Entry
import threading
import time
import math
import base64

window = tk.Tk()
window.title("Pichu symbolizers")
window.geometry('650x650')
window.configure(bg="#01d9e9")
# -MAIN VARS (IMPORTANT)
alpha = 1
beta = 0
gamma = 0
delta = 0
resetgamma = 0
resetdelta = 0
baseincrease = 1
up2multincrease = 1
milestoneincrease = 1
alphanizemulti = 1
alphanizebetamulti = 1
gammabooster = 1
challengerequirement = 1
challengecompletions = 0
challenge2requirement = 1
challenge2completions = 0
betagenboost = round(math.log10((beta + 1) * 10), 2)
betamaxboost = round(math.log10((beta + 1) * 10), 2)
betamaxmulti = round(betamaxboost, 2)
incre = (baseincrease * up2multincrease)
incre2 = (milestoneincrease * alphanizemulti)
incre3 = incre * incre2
incre4 = incre3 * gammabooster
incre5 = incre4 * betagenboost
increase = incre5 * ((2.5 * challengecompletions) + 1)
basemaxalpha = 100
betamaxmulti = 1
milestonemaxmulti = 1
alpmax = (basemaxalpha * betamaxmulti)
max_alpha = alpmax * milestonemaxmulti
rate = 1
alphapowerbooster = 1
alphapower = 0
deltaamount = 0
challengeactive = False
alphanizerunlocked = False
gammaifyunlocked = False
betagenerationunlocked = False
challenge2active = False
challengeunlocked = False
deltaunlocked = False
deltaresetcomplete = False
# -SIDE VARS (E)
acost1 = 10
a1buyamount = 0
acost2 = 100
a2buyamount = 0
betaify = 1e3
resetbeta = 0
betagenboost = math.log10((beta + 1) * 10)
betamaxboost = math.log10((beta + 1) * 10)
bcost1 = 10
milestoneamount = 0
bcost2 = 500
gupg1 = 10
g1buyamount = 0
gupg2 = 100
gupg3 = 1000
g3buyamount = 0
dupg1 = 1
d1buyamount = 0
# -
# -
progress_bar = ttk.Progressbar(window,
                               orient="horizontal",
                               length=300,
                               mode="determinate",
                               maximum=max_alpha)
progress_bar.grid(row=0, column=0, padx=10, pady=10)

alpha_label = tk.Label(window, text=f"Alpha: {alpha}/{max_alpha}")
alpha_label.grid(row=1, column=0, padx=10, pady=10)
alpha_label.configure(bg="ghostwhite")


# -SCREEN UPDATE START
def update():
    global acost1, a1buyamount, alpha, max_alpha, increase, rate, beta, betaify, resetbeta, milestoneamount
    global betaboost, betagenboost, betamaxboost, basemaxalpha, betamaxmulti, milestonemaxmulti, milestoneincrease, alphanizebetamulti, alphanizemulti, alphanizebetamulti
    global gammaifyunlocked, resetgamma, gamma, challengecompletions, challengerequirement, challengeunlocked, incre1, incre2, incre3, incre4, deltaunlocked, incre5

    while True:
        # Recalculation
        betagenboost = round(math.log10((beta + 1) * 10), 2)
        betamaxboost = round(math.log10((beta + 1) * 10), 2)
        betamaxmulti = round(betamaxboost, 2)

        max_alpha = math.floor(basemaxalpha * betamaxmulti * milestonemaxmulti)
        incre = round((baseincrease * up2multincrease), 2)
        incre2 = round((milestoneincrease * alphanizemulti), 2)
        incre3 = round(incre * incre2,2)
        incre4 = round(incre3 * gammabooster,2)
        incre5 = round(incre4 * betagenboost,2)
        increase = round((incre5 * ((2.5 * challengecompletions) + 1)), 2)

        # UI
        milestonelabel.configure(
            text=
            f"Your milestone boosts: {milestoneincrease}x α,  {milestonemaxmulti}x max α"
        )
        progress_bar.configure(maximum=max_alpha)
        alpha_label.config(
            text=
            f"Alpha: {alpha}/{max_alpha} , +{increase:.1f}α / {rate}s , Beta: {beta}β , {resetbeta}β/reset"
        )
        aupg1.configure(text=f"{acost1} α")
        doubleup.configure(text=f"Buy ({a1buyamount})")
        aupg2.configure(text=f"{acost2} α")
        increasemax.configure(text=f"Buy ({a2buyamount})")
        betaboost.configure(
            text=
            f"Beta boosts the generation by {betagenboost}x and max by {betamaxboost}x"
        )
        betareset.configure(text=f"Generate {resetbeta} β")
        milestonebutton.configure(text=f"Increase milestone ({milestoneamount})")
        alphanizeboostlabel.configure(
            text=f"Alphanizer boosts both multi by {alphanizemulti}")
        bupg1.configure(text=str(bcost1) + " β")
        # RESET STUFF LOL

        resetbeta = math.floor(((math.log10(alpha + 1) * math.log2(
            (max_alpha) / 3)) * (1 + alphanizebetamulti)) *
                               ((0.25 * challengecompletions) + 1))
        resetgamma = round(
            (((math.sqrt(beta) * (alpha / 1e4)) * ((alpha * 1.2) / max_alpha)) / 10), 2)
        if alphanizerunlocked and not alphanizer_thread.is_alive():
            alphanizer_thread.start()
            pass
        # UNLOCK GAMMA N GAMMA STUFF
        if beta >= 3000 and not gammaifyunlocked:
            print("OUTPUT: GAMMAIFY UNLOCKED!!!")
            new_window.title("Gammaify!")
            new_label.configure(text="Perform a gamma....")
            new_button.configure(text=f"Perform a γ for {resetgamma}",
                                 command=gammareset)
            gammaifyunlocked = True
            gammaup1label.configure(text=f"{gupg1} γ")
            gammaup1button.configure(text=f"Buy ({g1buyamount})", command=gammaupg1)
            gammaup1explain.configure(
                text="Increases a delta multiplier by + 1.5x, boosts alpha and alpha power and lowers rate.")
        if gammaifyunlocked:
            new_button.configure(text=f"Perform a γ for {resetgamma}")
            gamma = round(gamma, 2)
            gammadisplay.configure(text=f"{gamma}")
            gammaup1label.configure(text=f"{gupg1} γ")
            gammaup1button.configure(text=f"Buy ({g1buyamount})")
            gammaupg2label.configure(text=f"{gupg2} γ")
            gammaup2button.configure(text=f"Try ({challengecompletions}) ({challengeactive})", command=gammaupg2)
            gammaupg2explain.configure(text=f"Commits a gamma reset. Getting increasing amount of beta increases beta.")
        if challengecompletions >= 10 and not challengeunlocked:
            gammaupg3label.configure(text=f"{gupg3} γ")
            gammaup3button.configure(text=f"Try ({g3buyamount}) ({challenge2active})")
            gammaupg3explain.configure(text=f"Unlock inner potential...?")
            challengeunlocked = True
        if challengeunlocked:
            gammaupg3label.configure(text=f"{gupg3} γ")
            gammaup3button.configure(text=f"Buy ({g3buyamount})")
            gammaupg3explain.configure(text=f"Unlock inner potential...?")
        if gamma >= 3000 and challenge2completions >= 0:
            print("OUTPUT: Darkness seeps around you...")
            print("OUTPUT: DELTAIFY UNLOCKED?!?!")
            deltaunlocked = True
        if deltaunlocked:
            deltalabel.configure(text="You need 3000 gamma and a challenge 2 completion to prove yourself worthy.")
            deltaresetbutton.configure(text=f"Accept it. {resetdelta} δ awaits...", command= deltareset)
        time.sleep(0.25)


# -SCREEN UPDATE END


# -ALPHA UPDATE FUNCTION START
def update_alpha():
    global alpha, increase, rate, softcapmulti, max_alpha

    while True:
        increment = increase
        increase = round(increase, 1)
        alpha += increment
        alpha = round(alpha, 1)
        if alpha > max_alpha:
            alpha = max_alpha
        progress_bar["value"] = alpha
        alpha_label.config(
            text=
            f"Alpha: {alpha}/{max_alpha} , +{increase}α / {rate}s , Beta: {beta}β , {resetbeta}β/reset"
        )

        window.update()
        time.sleep(rate)


# -ALPHA UPDATE FUNCTION END


# -ALPHA UPGRADE 1 START
def alphaupgrade1():
    global alpha, baseincrease, acost1, a1buyamount
    if alpha >= acost1:
        alpha -= acost1
        acost1 = math.floor(5 + (acost1 * (1.05 * (1 + (a1buyamount / 100)))))
        baseincrease += 1
        a1buyamount += 1
    else:
        print("WARN: Not enough alpha!")


aupg1 = Label(window, text=str(acost1) + " α")
aupg1.grid(column=0, row=10)
aupg1.configure(bg="ghostwhite")

doublelabel = Label(window, text="+ 1x α per second.")
doublelabel.grid(column=20, row=10)
doublelabel.configure(bg="ghostwhite")

doubleup = Button(window,
                  text=f"Buy ({str(a1buyamount)})",
                  command=alphaupgrade1)
doubleup.grid(column=10, row=10)


# -ALPHA UPGRADE 1 END


# -ALPHA UPGRADE 2 START
def alphaupgrade2():
    global alpha, basemaxalpha, acost2, a2buyamount, max_alpha, progress_bar, up2multincrease
    if a2buyamount == 10:
        print("WARN: Maxed out!")
    if alpha >= acost2:
        alpha -= acost2
        acost2 *= math.floor(2 * (1 + (1.5 ** (a2buyamount - 5))))
        basemaxalpha *= 2
        up2multincrease += 1.5
        progress_bar.configure(maximum=max_alpha)
        a2buyamount += 1
        if a2buyamount == 10:
            print("OUTPUT: MAX ALPHA UPGRADE 2 REACHED!")
            acost2 = 1e999
    else:
        print("WARN: Not enough alpha!")


aupg2 = Label(window, text=str(acost2) + " α")
aupg2.grid(column=0, row=20)
aupg2.configure(bg="ghostwhite")
maxincreaselabel = Label(window, text="x2 α maximum + x1.5 α generation")
maxincreaselabel.grid(column=20, row=20)
maxincreaselabel.configure(bg="ghostwhite")
increasemax = Button(window,
                     text=f"Buy ({str(a2buyamount)})",
                     command=alphaupgrade2)
increasemax.grid(column=10, row=20)


# -ALPHA UPGRADE 2 END


# -ALPHA UPGRADE 3 START
def betaresetcommand():
    global beta, alpha, max_alpha, resetbeta, a1buyamount, a2buyamount, acost1, acost2, alpmax
    global betagenboost, betamaxboost, up2multincrease, baseincrease, increase, rate, basemaxalpha, milestonemaxmulti
    resetbeta = math.floor(((math.log10(alpha + 1) * math.log2(
        (max_alpha) / 3)) * (1 + alphanizebetamulti)) *
                           ((0.25 * challengecompletions) + 1))
    if alpha > 1e3:
        beta += resetbeta
        baseincrease = 1
        alpha = 0
        basemaxalpha = 100
        a1buyamount = 0
        a2buyamount = 0
        up2multincrease = 1
        acost1 = 10
        acost2 = 100
        max_alpha = alpmax * milestonemaxmulti
        betagenboost = round((math.log10((beta + 1) * 10)), 2)
        betamaxboost = round((math.log10((beta + 1) * 10)), 2)
        progress_bar.configure(maximum=max_alpha)
        alpha_label.config(
            text=f"Alpha: {alpha}/{max_alpha} , +{increase}α / {rate}s")
        betareset.configure(text=f"Generate {resetbeta} β")
        betaboost.configure(
            text=
            f"Beta boosts the generation by {betagenboost}x and max by {betamaxboost}"
        )
        print(
            f"OUTPUT: Beta reset performed. Performed for {resetbeta}. Total: {beta}"
        )
        resetbeta = 0
    else:
        print("WARN: Alpha is not high enough to create Beta.")


atob = Label(window, text=str(betaify) + " α")
atob.grid(column=0, row=40)
atob.configure(bg="ghostwhite")

atoblabel = Label(window, text="Converts Alpha into Beta.")
atoblabel.grid(column=20, row=40)
atoblabel.configure(bg="ghostwhite")

betareset = Button(window,
                   text=f"Generate {resetbeta} β",
                   command=betaresetcommand)
betareset.grid(column=10, row=40)

betaboost = Label(
    window,
    text=
    f"Beta boosts the generation by {betagenboost}x and max by {betamaxboost}")
betaboost.grid(column=10, row=55)
betaboost.configure(bg="ghostwhite")


# -ALPHA UPGRADE 3 END


# -BETA UPGRADE 1 START
def milestones():
    global beta, milestoneamount, bcost1, milestonemaxmulti, milestoneincrease, betagenerationunlocked
    if beta > bcost1:
        # -MILESTONE STUFF
        beta -= bcost1
        bcost1 = round((bcost1 * 9.5))
        bupg1.configure(text=str(bcost1) + " β")
        milestoneamount += 1
        if milestoneamount == 1:
            print("OUTPUT: MILESTONE 1 UNLOCKED\n +25% Alpha per milestone!")
            milestoneincrease = round((milestoneincrease * 1.25), 2)
        elif milestoneamount == 2:
            print("OUTPUT: MILESTONE 2 UNLOCKED\n x2 Maximum Alpha per milestone!")
            milestoneincrease = round((milestoneincrease * 1.25), 2)
            milestonemaxmulti = round((milestonemaxmulti * 2), 2)
        elif milestoneamount == 5:
            print(
                "OUTPUT: MILESTONE 5 UNLOCKED\n Generate 10% of beta on beta reset!")
            betagenerationunlocked = True
            milestoneincrease = round((milestoneincrease * 1.25), 2)
            milestonemaxmulti = round((milestonemaxmulti * 2), 2)
            betagenerationthread.start()
        else:
            print(f"OUTPUT: MILESTONE {milestoneamount} REACHED!")
            milestoneincrease = round((milestoneincrease * 1.25), 2)
            milestonemaxmulti = round((milestonemaxmulti * 2), 2)

    else:
        print("WARN: Not enough beta!")


bupg1 = Label(window, text=str(bcost1) + " β")
bupg1.grid(column=0, row=60)
bupg1.configure(bg="ghostwhite")

bupg1label = Label(window,
                   text="Increases milestones, generating extra resources!")
bupg1label.grid(column=20, row=60)
bupg1label.configure(bg="ghostwhite")

milestonebutton = Button(window,
                         text=f"Increase milestone ({milestoneamount})",
                         command=milestones)
milestonebutton.grid(column=10, row=60)

milestonelabel = Label(
    window,
    text=
    f"Your milestone boosts: {milestoneincrease}x α,  {milestonemaxmulti}x max α"
)
milestonelabel.configure(bg="ghostwhite")
milestonelabel.grid(column=10, row=65)


# -BETA UPGRADE 1 END

# -BETA UPGRADE 2 START


def alphanizer():
    global beta, alpha, alphanizemulti, alphanizebetamulti, bcost2, alphanizerunlocked
    if beta >= bcost2:
        beta -= bcost2
        alphanizerunlocked = True
        bcost2 = math.nan
        alpherupglabel.configure(
            text=
            f"Unlocks the alphanizer, which generates boosts / second. ({alphanizerunlocked})"
        )
        print("OUTPUT: Alphanizer active.")
        alpherupg.configure(text="inf β")
        if not alphanizer_thread.is_alive():
            alphanizer_thread.start()
    else:
        print("WARN: Not enough beta.")


alpherupg = Label(window, text=str(bcost2) + " β")
alpherupg.grid(column=0, row=70)
alpherupg.configure(bg="ghostwhite")

alpherupglabel = Label(
    window,
    text=
    f"Unlocks the alphanizer, which generates boosts / second. ({alphanizerunlocked})"
)
alpherupglabel.grid(column=20, row=70)
alpherupglabel.configure(bg="ghostwhite")

alphaunlockbutton = Button(window,
                           text="Unlock the alphanizer...",
                           command=alphanizer)
alphaunlockbutton.grid(column=10, row=70)

alphanizeboostlabel = Label(
    window, text=f"Alphanizer boosts both multi by {alphanizemulti}")
alphanizeboostlabel.grid(column=10, row=75)
alphanizeboostlabel.configure(bg="ghostwhite")


# -BETA UPGRADE 2 END
# -BETA ALPHANIZER START


def alphanizemachine():
    global alphanizebetamulti, alphanizemulti, alphapower, gammabooster
    while alphanizerunlocked:
        alphapower += (0.1 * gammabooster)
        alphanizebetamulti = 1 + (round(math.log2(math.sqrt(alphapower)), 2))
        alphanizemulti = 1 + (round(math.log2(math.sqrt(alphapower)), 2))
        time.sleep(0.1)


# -BETA ALPHANIZER END


# -BETA GENERATION START
def betageneration():
    global beta, resetbeta, betagenerationunlocked
    while betagenerationunlocked:
        beta += round((resetbeta / 10))
        time.sleep(0.1)


# -BETA GENERATION END

# -Thread START
alpha_thread = threading.Thread(target=update_alpha)
alpha_thread.start()
update_thread = threading.Thread(target=update)
update_thread.start()
betagenerationthread = threading.Thread(target=betageneration)
alphanizer_thread = threading.Thread(target=alphanizemachine)
# -Thread END

# -SECOND WINDOW

new_window = tk.Toplevel(window)
new_window.title("??? [3,000 Beta Required!]")
new_window.geometry('500x500')
new_window.configure(bg="#C72EC7")

new_label = tk.Label(new_window, text="???")
new_label.grid(column=0, row=0)
new_label.configure(bg="#C72EC7")

new_button = tk.Button(new_window, text="???", command=lambda: None)
new_button.grid(column=10, row=0)
new_button.configure(bg="ghostwhite")

gammadisplay = tk.Label(new_window, text="???")
gammadisplay.grid(column=20,row=0)
gammadisplay.configure(bg="#C72EC7")

gammaup1label = tk.Label(new_window, text="???")
gammaup1label.grid(column=0, row=10)
gammaup1label.configure(bg="#C72EC7")

gammaup1button = tk.Button(new_window, text="???", command=lambda: None)
gammaup1button.grid(column=10, row=10)
gammaup1button.configure(bg="ghostwhite")

gammaup1explain = tk.Label(new_window, text="???")
gammaup1explain.grid(column=20, row=10)
gammaup1explain.configure(bg="#C72EC7")

gammaupg2label = tk.Label(new_window, text="???")
gammaupg2label.grid(column=0, row=20)
gammaupg2label.configure(bg="#C72EC7")

gammaup2button = tk.Button(new_window, text="???", command=lambda: None)
gammaup2button.grid(column=10, row=20)
gammaup2button.configure(bg="ghostwhite")

gammaupg2explain = tk.Label(new_window, text="???")
gammaupg2explain.grid(column=20, row=20)
gammaupg2explain.configure(bg="#C72EC7")

gammaupg3label = tk.Label(new_window, text="???")
gammaupg3label.grid(column=0, row=30)
gammaupg3label.configure(bg="#C72EC7")

gammaup3button = tk.Button(new_window, text="???", command=lambda: None)
gammaup3button.grid(column=10, row=30)
gammaup3button.configure(bg="ghostwhite")

gammaupg3explain = tk.Label(new_window, text="???")
gammaupg3explain.grid(column=20, row=30)
gammaupg3explain.configure(bg="#C72EC7")


# -RESET START

def gammareset():
    global beta, alpha, max_alpha, gamma, resetgamma, baseincrease, basemaxalpha, a1buyamount, a2buyamount, up2multincrease, acost1, acost2, bcost1, bcost2
    global betamaxboost, betagenboost, rate, alphapower, alphanizerunlocked, milestoneincrease, milestonemaxmulti, milestoneamount, betagenerationunlocked, alphanizebetamulti, alphanizemulti
    if beta >= 3000:
        resetgamma = round(
        (((math.sqrt(beta) * (alpha / 1e4)) * ((alpha * 1.2) / max_alpha)) / 10), 2)
        gamma += resetgamma
        print(f"OUTPUT: GAMMA RESET PERFORMED FOR {resetgamma}")
        baseincrease = 1
        alpha = 0
        beta = 0
        basemaxalpha = 100
        a1buyamount = 0
        a2buyamount = 0
        up2multincrease = 1
        acost1 = 10
        acost2 = 100
        bcost1 = 10
        bcost2 = 500
        max_alpha = alpmax * milestonemaxmulti
        alphapower = 1
        alphanizerunlocked = False
        alpherupglabel.configure(text=f"Unlocks the alphanizer, which generates boosts / second. ({alphanizerunlocked})")
        alphanizemulti = 1
        alphanizebetamulti = 1
        milestoneamount = 0
        milestoneincrease = 1
        milestonemaxmulti = 1
        betagenerationunlocked = False
        betagenboost = round((math.log10((beta + 1) * 10)), 2)
        betamaxboost = round((math.log10((beta + 1) * 10)), 2)
        progress_bar.configure(maximum=max_alpha)
        alpha_label.config(
            text=f"Alpha: {alpha}/{max_alpha} , +{increase}α / {rate}s")
        betareset.configure(text=f"Generate {resetbeta} β")
        betaboost.configure(
            text=
            f"Beta boosts the generation by {betagenboost}x and max by {betamaxboost}"
        )


# -RESET END

# -GAMMA UPGRADE 1 START
def gammaupg1():
    global gupg1, gamma, rate, g1buyamount, gammabooster
    if gamma >= gupg1:
        gamma -= gupg1
        gupg1 = round(gupg1 * 1.5, 2)
        rate = round((rate * 0.9), 2)
        gammabooster += 1.5
        g1buyamount += 1
    else:
        print("WARN: Not enough gamma!")


# -GAMMA UPGRADE 1 END

# -GAMMA UPGRADE 2 START

def gammaupg2():
    global gupg2, gamma, g2buyamount, challengeactive, challengecompletions, beta, challengerequirement
    if gamma >= gupg2:
        print("OUTPUT: Get Beta to level up this challenge.")
        print(
            "OUTPUT: Gain +0.25x beta for every challenge completion."
        )
        print(
            f"OUTPUT: You have completed challenge 1: {challengecompletions} times."
        )
        if not challengeactive:
            challengeactive = True
            gammaup2button.configure(text=f"Buy ({challengecompletions}) ({challengeactive})")
            if not challenge_thread.is_alive():
                challenge_thread.start()
            gammareset()
        elif challengeactive:
            challengeactive = False
            gammaup2button.configure(text=f"Buy ({challengecompletions}) ({challengeactive})")
            print(
                f"OUTPUT: You have completed challenge 1: {challengecompletions} times."
            )
            while beta >= challengerequirement:
                challengerequirement *= 2
                challengecompletions += 1

            gammareset()
    else:
        print("WARN: Not enough gamma!")


def challengechecker():
    global milestoneamount, challengerequirement, challengecompletions, challengeactive
    if challengeactive:
        while milestoneamount >= challengerequirement:
            challengerequirement += 1
            challengecompletions += 1
            time.sleep(1)


# -GAMMA UPGRADE 2 END

# -GAMMA UPGRADE 3 START

def gammaupg3():
    global gamma, gupg3, challenge2active, deltaunlocked
    if gamma >= gupg3:
        print("OUTPUT: The suffering may begin.")
        time.sleep(0.5)
        print("OUTPUT: Good luck.")
        print("OUTPUT: Note: I recomend you get gamma.")
        if not challenge2active:
            challenge2active = True
            gammareset()
        if challenge2active:
            if challenge2requirement >= gamma:
                print("OUTPUT: Well done!")
                deltaunlocked = True
            else:
                print("OUTPUT: You have failed the challenge and quit.")
                gammareset()

    else:
        print("WARN: Not enough gamma!")


# -GAMMA UPGRADE 3 END

# -DELTAIFY, THE NEW RESET LAYER!!

deltalabel = tk.Label(new_window, text=f"...unworthy...")
deltalabel.grid(column=0,row=40)
deltalabel.configure(bg="#C72EC7")

deltaresetbutton = tk.Button(new_window, text=f"???", command= lambda: None)
deltaresetbutton.grid(column=0,row=50)
deltaresetbutton.configure(bg="ghostwhite")

def deltaresetstats():
    global alpha, beta, gamma, resetgamma, baseincrease, up2multincrease, milestoneincrease, alphanizemulti, alphanizebetamulti, gammabooster, challengerequirement
    global challengecompletions, challenge2requirement, challenge2completions, incre, incre2, incre3, incre4, increase, basemaxalpha, betamaxmulti, betamaxboost
    global milestonemaxmulti, alpmax, max_alpha, rate, alphapowerbooster, alphapower, challengeactive, alphanizerunlocked, betagenerationunlocked, challenge2active
    global challengeunlocked
    alpha = 1
    beta = 0
    gamma = 0
    resetgamma = 0
    baseincrease = 1
    up2multincrease = 1
    milestoneincrease = 1
    alphanizemulti = 1
    alphanizebetamulti = 1
    gammabooster = 1
    challengerequirement = 1
    challengecompletions = 0
    challenge2requirement = 1
    challenge2completions = 0
    incre = (baseincrease * up2multincrease)
    incre2 = (milestoneincrease * alphanizemulti)
    incre3 = incre * incre2
    incre4 = incre3 * gammabooster
    increase = incre4 * ((2.5 * challengecompletions) + 1)
    basemaxalpha = 100
    betamaxmulti = 1
    betamaxboost = 1
    milestonemaxmulti = 1
    alpmax = (basemaxalpha * betamaxmulti)
    max_alpha = alpmax * milestonemaxmulti
    rate = 1
    alphapowerbooster = 1
    alphapower = 0
    challengeactive = False
    alphanizerunlocked = False
    betagenerationunlocked = False
    challenge2active = False
    challengeunlocked = False

def deltareset():
    global gamma, beta, alpha, delta, resetdelta, max_alpha, deltaresetcomplete
    if gamma >= 3000 and challenge2completions != 0:
      resetdelta += (1*deltaamount)
      print("OUTPUT: Darkness is among you...")
      deltaresetcomplete = True
      deltaresetstats()
    else:
        print("WARN: The darkness perceives you as unworthy...")
        print("A whisper stands out:  '3000 gamma... complete challenge 2...' ")

def deltaupg1():
    global delta, dupg1, d1buyamount,incre4

# -DELTAIFY, THE NEW RESET LAYER ENDS...
# THREADS 2 YAY START

challenge_thread = threading.Thread(target=challengechecker)

# THREADS 2 YAY END

# SAVE STUFF, ALWAYS KEEP AT BOTTOM!!

# -SAVE GAME STUFF IDK START

savebutton = Button(window, text="Save", command=lambda: savecheckr())
savebutton.grid(column=0, row=100)
loadbutton = Button(window, text="Load", command=lambda: loadcheckr())
loadbutton.grid(column=0, row=110)

saveentry = Entry(window, width=10)
saveentry.grid(column=10, row=100)

loadentry = Entry(window, width=10)
loadentry.grid(column=10, row=110)


def save_variables_to_file():
    if not filenamechoice:
        print("WARN: No filename specified")
        return

    variables = [
        f"alpha={alpha}", f"beta={beta}", f"gamma={gamma}", f"delta={delta}",
        f"basemaxalpha={basemaxalpha}", f"betamaxmulti={betamaxmulti}",
        f"acost1={acost1}", f"acost2={acost2}", f"bcost1={bcost1}",
        f"bcost2={bcost2}", f"a1buyamount={a1buyamount}",
        f"a2buyamount={a2buyamount}", f"milestoneamount={milestoneamount}",
        f"gupg1={gupg1}", f"g1buyamount={g1buyamount}", f"gupg2={gupg2}",
        f"baseincrease={baseincrease}", f"up2multincrease={up2multincrease}",
        f"betamaxboost={betamaxboost}", f"milestoneincrease={milestoneincrease}",
        f"alphanizemulti={alphanizemulti}", f"alphanizebetamulti={alphanizebetamulti}",
        f"gammabooster={gammabooster}", f"challengerequirement={challengerequirement}",
        f"challengecompletions={challengecompletions}", f"challenge2completions={challenge2completions}",
        f"challenge2requirement={challenge2requirement}", f"incre={incre}",
        f"incre2={incre2}", f"incre3={incre3}", f"incre4={incre4}",
        f"increase={increase}", f"milestonemaxmulti={milestonemaxmulti}",
        f"alpmax={alpmax}", f"max_alpha={max_alpha}", f"rate={rate}",
        f"alphapowerbooster={alphapowerbooster}", f"alphapower={alphapower}",
        f"challengeactive={challengeactive}", f"alphanizerunlocked={alphanizerunlocked}",
        f"gammaifyunlocked={gammaifyunlocked}", f"betagenerationunlocked={betagenerationunlocked}",
        f"challengeunlocked={challengeunlocked}", f"deltaunlocked={deltaunlocked}",
        f"deltaresetcomplete={deltaresetcomplete}"
    ]

    content = ""
    for i in range(0, len(variables), 10):
        chunk = variables[i:i + 10]
        content += "{" + ",".join(chunk) + "}\n"
    
    encoded_content = base64.b64encode(content.encode()).decode()
    
    with open(f"saves/{filenamechoice}.txt", 'w') as f:
        f.write(encoded_content)


def retrieve_variables_from_file():
    if not filenamechoice:
        print("WARN: No filename specified")
        return
    global alpha, beta, gamma, baseincrease, up2multincrease, milestoneincrease
    global alphanizemulti, alphanizebetamulti, gammabooster, challengerequirement
    global challengecompletions, incre, incre2, incre3, incre4, increase
    global milestonemaxmulti, alpmax, max_alpha, rate, alphapowerbooster
    global alphapower, challengeactive, alphanizerunlocked, gammaifyunlocked
    global betagenerationunlocked, a1buyamount, a2buyamount, acost1, acost2, milestoneamount, bcost1, bcost2, g1buyamount, gupg1, g1buyamount, gupg2, g2buyamount
    global betamaxboost, betamaxmulti, basemaxalpha, challengeunlocked, challenge2requirement, challenge2completions, deltaunlocked

    with open(f"saves/{filenamechoice}.txt", 'r') as f:
        encoded_content = f.read()
        decoded_content = base64.b64decode(encoded_content).decode()
        lines = decoded_content.split('\n')
        for line in lines:
            variables = line.strip()[1:-1].split(',')  # Remove { } and split
            for var in variables:
                if not var: continue
                name, value = var.strip().split('=')
                if value.lower() == 'true':
                    value = True
                elif value.lower() == 'false':
                    value = False
                else:
                    try:
                        value = float(value) if '.' in value else int(value)
                    except ValueError:
                        print(f"WARN: Could not convert {value} to number")
                        continue
                globals()[name] = value

        # Update UI elements after loading
        progress_bar.configure(maximum=max_alpha)
        alpha_label.config(
            text=
            f"Alpha: {alpha}/{max_alpha} , +{increase}α / {rate}s , Beta: {beta}β , {resetbeta}β/reset"
        )
        milestonelabel.configure(
            text=
            f"Your milestone boosts: {milestoneincrease}x α,  {milestonemaxmulti}x max α"
        )
        betaboost.configure(
            text=
            f"Beta boosts the generation by {betagenboost}x and max by {betamaxboost}x"
        )
        alphanizeboostlabel.configure(
            text=f"Alphanizer boosts both multi by {alphanizemulti:.1f}")

        # Start threads based on boolean states
        if betagenerationunlocked and not betagenerationthread.is_alive():
            betagenerationthread.start()
        if alphanizerunlocked and not alphanizer_thread.is_alive():
            alphanizer_thread.start()
        if gammaifyunlocked:
            new_window.title("Gammaify!")
            new_label.configure(text="Perform a gamma....")
            new_button.configure(text=f"Perform a γ for {resetgamma}",
                                 command=gammareset)
            gammaup1label.configure(text=f"{gupg1} γ")
            gammaup1button.configure(text=f"Buy ({g1buyamount})", command=gammaupg1)
            gammaup1explain.configure(
                text="Increases a gamma multiplier by + 1.5x, boosts alpha and alpha power and lowers rate.")


def savecheckr():
    global filenamechoice, challengeactive, challenge2active
    if challengeactive or challenge2active:
        print("WARN: Failure to save in challenge.")
    if not challengeactive or not challenge2active:
        if saveentry.get() == "":
            print("WARN: No save name entered.")
        else:
            print(f"INFO: Save name entered. Saving {saveentry.get()}")
            filenamechoice = saveentry.get()
            save_variables_to_file()


def loadcheckr():
    global filenamechoice, challengeactive, challenge2active
    if challengeactive or challenge2active:
        print("WARN: Failure to load in challenge.")
    if not challengeactive or not challenge2active:
        if loadentry.get() == "":
            print("WARN: No load name entered.")
        else:
            print(f"INFO: Load name entered. Loading {loadentry.get()}.")
            filenamechoice = loadentry.get()
            retrieve_variables_from_file()


# -SAVE GAME STUFF IDK END

# SAVE STUFF END!
window.mainloop()
