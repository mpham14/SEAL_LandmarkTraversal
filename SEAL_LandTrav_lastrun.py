#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Mon Mar 13 16:33:27 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'SEAL_LandTrav'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/mettapham/Downloads/SEAL-selected/SEAL_LandmarkTraversal/SEAL_LandTrav_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Welcome" ---
text = visual.TextStim(win=win, name='text',
    text='Welcome to the SEAL Landmark Traversal Task',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Instruction" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='In this task, you are presented with a picture of an object\n\nYour task is to find the object \n\nPress Upper or Lower to start',
    font='Open Sans',
    pos=(0, 0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Upper_button = visual.ButtonStim(win, 
    text='Upper', font='Arvo',
    pos=(-.3,-.18),
    letterHeight=0.05,
    size=(.4,.2), borderWidth=3.0,
    fillColor='darkgrey', borderColor='white',
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Upper_button'
)
Upper_button.buttonClock = core.Clock()
Lower_button = visual.ButtonStim(win, 
    text='Lower', font='Arvo',
    pos=(0.3, -.18),
    letterHeight=0.05,
    size=(.4,.2), borderWidth=3.0,
    fillColor='darkgrey', borderColor='white',
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Lower_button'
)
Lower_button.buttonClock = core.Clock()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "Lower_trial" ---
Landmark = visual.ImageStim(
    win=win,
    name='Landmark', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_4 = visual.TextStim(win=win, name='text_4',
    text='Please find this object\n\n',
    font='Open Sans',
    pos=(0, .35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
yesbutton = visual.ButtonStim(win, 
    text='', font='Arvo',
    pos=(-.2, -.4),
    letterHeight=0.05,
    size=(.25, .15), borderWidth=3.0,
    fillColor='darkgrey', borderColor='white',
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='yesbutton'
)
yesbutton.buttonClock = core.Clock()
nobutton = visual.ButtonStim(win, 
    text='', font='Arvo',
    pos=(0.2, -.4),
    letterHeight=0.05,
    size=(.25,.15), borderWidth=3.0,
    fillColor='darkgrey', borderColor='white',
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='nobutton'
)
nobutton.buttonClock = core.Clock()

# --- Initialize components for Routine "Upper_trial" ---
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_5 = visual.TextStim(win=win, name='text_5',
    text='Please find this object',
    font='Open Sans',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
yes_button = visual.ButtonStim(win, 
    text='', font='Arvo',
    pos=(-.2, -.4),
    letterHeight=0.05,
    size=[.25,.15], borderWidth=3.0,
    fillColor='darkgrey', borderColor='white',
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='yes_button'
)
yes_button.buttonClock = core.Clock()
no_button = visual.ButtonStim(win, 
    text='', font='Arvo',
    pos=(.2, -.4),
    letterHeight=0.05,
    size=[.25,.15], borderWidth=3.0,
    fillColor='darkgrey', borderColor='white',
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='no_button'
)
no_button.buttonClock = core.Clock()

# --- Initialize components for Routine "End" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
WelcomeComponents = [text]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcome" ---
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.stopped')
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome" ---
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# --- Prepare to start Routine "Instruction" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
mouse.x = []
mouse.y = []
mouse.leftButton = []
mouse.midButton = []
mouse.rightButton = []
mouse.time = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
InstructionComponents = [text_2, Upper_button, Lower_button, mouse]
for thisComponent in InstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instruction" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_2.started')
        text_2.setAutoDraw(True)
    
    # *Upper_button* updates
    if Upper_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Upper_button.frameNStart = frameN  # exact frame index
        Upper_button.tStart = t  # local t and not account for scr refresh
        Upper_button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Upper_button, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Upper_button.started')
        Upper_button.setAutoDraw(True)
    if Upper_button.status == STARTED:
        # check whether Upper_button has been pressed
        if Upper_button.isClicked:
            if not Upper_button.wasClicked:
                Upper_button.timesOn.append(Upper_button.buttonClock.getTime()) # store time of first click
                Upper_button.timesOff.append(Upper_button.buttonClock.getTime()) # store time clicked until
            else:
                Upper_button.timesOff[-1] = Upper_button.buttonClock.getTime() # update time clicked until
            if not Upper_button.wasClicked:
                None
            Upper_button.wasClicked = True  # if Upper_button is still clicked next frame, it is not a new click
        else:
            Upper_button.wasClicked = False  # if Upper_button is clicked next frame, it is a new click
    else:
        Upper_button.wasClicked = False  # if Upper_button is clicked next frame, it is a new click
    
    # *Lower_button* updates
    if Lower_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Lower_button.frameNStart = frameN  # exact frame index
        Lower_button.tStart = t  # local t and not account for scr refresh
        Lower_button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Lower_button, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Lower_button.started')
        Lower_button.setAutoDraw(True)
    if Lower_button.status == STARTED:
        # check whether Lower_button has been pressed
        if Lower_button.isClicked:
            if not Lower_button.wasClicked:
                Lower_button.timesOn.append(Lower_button.buttonClock.getTime()) # store time of first click
                Lower_button.timesOff.append(Lower_button.buttonClock.getTime()) # store time clicked until
            else:
                Lower_button.timesOff[-1] = Lower_button.buttonClock.getTime() # update time clicked until
            if not Lower_button.wasClicked:
                None
            Lower_button.wasClicked = True  # if Lower_button is still clicked next frame, it is not a new click
        else:
            Lower_button.wasClicked = False  # if Lower_button is clicked next frame, it is a new click
    else:
        Lower_button.wasClicked = False  # if Lower_button is clicked next frame, it is a new click
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse.started', t)
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                buttons = mouse.getPressed()
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(mouse.mouseClock.getTime())
                
                continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instruction" ---
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Upper_button.numClicks', Upper_button.numClicks)
if Upper_button.numClicks:
   thisExp.addData('Upper_button.timesOn', Upper_button.timesOn)
   thisExp.addData('Upper_button.timesOff', Upper_button.timesOff)
else:
   thisExp.addData('Upper_button.timesOn', "")
   thisExp.addData('Upper_button.timesOff', "")
thisExp.addData('Lower_button.numClicks', Lower_button.numClicks)
if Lower_button.numClicks:
   thisExp.addData('Lower_button.timesOn', Lower_button.timesOn)
   thisExp.addData('Lower_button.timesOff', Lower_button.timesOff)
else:
   thisExp.addData('Lower_button.timesOn', "")
   thisExp.addData('Lower_button.timesOff', "")
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse.x', mouse.x)
thisExp.addData('mouse.y', mouse.y)
thisExp.addData('mouse.leftButton', mouse.leftButton)
thisExp.addData('mouse.midButton', mouse.midButton)
thisExp.addData('mouse.rightButton', mouse.rightButton)
thisExp.addData('mouse.time', mouse.time)
thisExp.nextEntry()
# Run 'End Routine' code from code
if mouse.isPressedIn(Upper_button):
    UpperTrialReps = 1
    LowerTrialReps = 0
    
elif mouse.isPressedIn(Lower_button):
    UpperTrialReps = 0
    LowerTrialReps = 1

    
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
ShowLowerLandtrials_Loop = data.TrialHandler(nReps=LowerTrialReps, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='ShowLowerLandtrials_Loop')
thisExp.addLoop(ShowLowerLandtrials_Loop)  # add the loop to the experiment
thisShowLowerLandtrials_Loop = ShowLowerLandtrials_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisShowLowerLandtrials_Loop.rgb)
if thisShowLowerLandtrials_Loop != None:
    for paramName in thisShowLowerLandtrials_Loop:
        exec('{} = thisShowLowerLandtrials_Loop[paramName]'.format(paramName))

for thisShowLowerLandtrials_Loop in ShowLowerLandtrials_Loop:
    currentLoop = ShowLowerLandtrials_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisShowLowerLandtrials_Loop.rgb)
    if thisShowLowerLandtrials_Loop != None:
        for paramName in thisShowLowerLandtrials_Loop:
            exec('{} = thisShowLowerLandtrials_Loop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    LowerLand_trials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('LandmarkTrav_Stimuli.xlsx'),
        seed=None, name='LowerLand_trials')
    thisExp.addLoop(LowerLand_trials)  # add the loop to the experiment
    thisLowerLand_trial = LowerLand_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLowerLand_trial.rgb)
    if thisLowerLand_trial != None:
        for paramName in thisLowerLand_trial:
            exec('{} = thisLowerLand_trial[paramName]'.format(paramName))
    
    for thisLowerLand_trial in LowerLand_trials:
        currentLoop = LowerLand_trials
        # abbreviate parameter names if possible (e.g. rgb = thisLowerLand_trial.rgb)
        if thisLowerLand_trial != None:
            for paramName in thisLowerLand_trial:
                exec('{} = thisLowerLand_trial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Lower_trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        Landmark.setImage(imageL)
        yesbutton.setText('Yes')
        nobutton.setText('No')
        # keep track of which components have finished
        Lower_trialComponents = [Landmark, text_4, yesbutton, nobutton]
        for thisComponent in Lower_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Lower_trial" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Landmark* updates
            if Landmark.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Landmark.frameNStart = frameN  # exact frame index
                Landmark.tStart = t  # local t and not account for scr refresh
                Landmark.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Landmark, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Landmark.started')
                Landmark.setAutoDraw(True)
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_4.started')
                text_4.setAutoDraw(True)
            
            # *yesbutton* updates
            if yesbutton.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                yesbutton.frameNStart = frameN  # exact frame index
                yesbutton.tStart = t  # local t and not account for scr refresh
                yesbutton.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(yesbutton, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'yesbutton.started')
                yesbutton.setAutoDraw(True)
            if yesbutton.status == STARTED:
                # check whether yesbutton has been pressed
                if yesbutton.isClicked:
                    if not yesbutton.wasClicked:
                        yesbutton.timesOn.append(yesbutton.buttonClock.getTime()) # store time of first click
                        yesbutton.timesOff.append(yesbutton.buttonClock.getTime()) # store time clicked until
                    else:
                        yesbutton.timesOff[-1] = yesbutton.buttonClock.getTime() # update time clicked until
                    if not yesbutton.wasClicked:
                        continueRoutine = False  # end routine when yesbutton is clicked
                        None
                    yesbutton.wasClicked = True  # if yesbutton is still clicked next frame, it is not a new click
                else:
                    yesbutton.wasClicked = False  # if yesbutton is clicked next frame, it is a new click
            else:
                yesbutton.wasClicked = False  # if yesbutton is clicked next frame, it is a new click
            
            # *nobutton* updates
            if nobutton.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                nobutton.frameNStart = frameN  # exact frame index
                nobutton.tStart = t  # local t and not account for scr refresh
                nobutton.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(nobutton, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'nobutton.started')
                nobutton.setAutoDraw(True)
            if nobutton.status == STARTED:
                # check whether nobutton has been pressed
                if nobutton.isClicked:
                    if not nobutton.wasClicked:
                        nobutton.timesOn.append(nobutton.buttonClock.getTime()) # store time of first click
                        nobutton.timesOff.append(nobutton.buttonClock.getTime()) # store time clicked until
                    else:
                        nobutton.timesOff[-1] = nobutton.buttonClock.getTime() # update time clicked until
                    if not nobutton.wasClicked:
                        continueRoutine = False  # end routine when nobutton is clicked
                        None
                    nobutton.wasClicked = True  # if nobutton is still clicked next frame, it is not a new click
                else:
                    nobutton.wasClicked = False  # if nobutton is clicked next frame, it is a new click
            else:
                nobutton.wasClicked = False  # if nobutton is clicked next frame, it is a new click
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Lower_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Lower_trial" ---
        for thisComponent in Lower_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        LowerLand_trials.addData('yesbutton.numClicks', yesbutton.numClicks)
        if yesbutton.numClicks:
           LowerLand_trials.addData('yesbutton.timesOn', yesbutton.timesOn)
           LowerLand_trials.addData('yesbutton.timesOff', yesbutton.timesOff)
        else:
           LowerLand_trials.addData('yesbutton.timesOn', "")
           LowerLand_trials.addData('yesbutton.timesOff', "")
        LowerLand_trials.addData('nobutton.numClicks', nobutton.numClicks)
        if nobutton.numClicks:
           LowerLand_trials.addData('nobutton.timesOn', nobutton.timesOn)
           LowerLand_trials.addData('nobutton.timesOff', nobutton.timesOff)
        else:
           LowerLand_trials.addData('nobutton.timesOn', "")
           LowerLand_trials.addData('nobutton.timesOff', "")
        # the Routine "Lower_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'LowerLand_trials'
    
# completed LowerTrialReps repeats of 'ShowLowerLandtrials_Loop'


# set up handler to look after randomisation of conditions etc
ShowUpperLandtrials_Loop = data.TrialHandler(nReps=UpperTrialReps, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='ShowUpperLandtrials_Loop')
thisExp.addLoop(ShowUpperLandtrials_Loop)  # add the loop to the experiment
thisShowUpperLandtrials_Loop = ShowUpperLandtrials_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisShowUpperLandtrials_Loop.rgb)
if thisShowUpperLandtrials_Loop != None:
    for paramName in thisShowUpperLandtrials_Loop:
        exec('{} = thisShowUpperLandtrials_Loop[paramName]'.format(paramName))

for thisShowUpperLandtrials_Loop in ShowUpperLandtrials_Loop:
    currentLoop = ShowUpperLandtrials_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisShowUpperLandtrials_Loop.rgb)
    if thisShowUpperLandtrials_Loop != None:
        for paramName in thisShowUpperLandtrials_Loop:
            exec('{} = thisShowUpperLandtrials_Loop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    UpperLand_trials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('LandmarkTrav_Stimuli.xlsx'),
        seed=None, name='UpperLand_trials')
    thisExp.addLoop(UpperLand_trials)  # add the loop to the experiment
    thisUpperLand_trial = UpperLand_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisUpperLand_trial.rgb)
    if thisUpperLand_trial != None:
        for paramName in thisUpperLand_trial:
            exec('{} = thisUpperLand_trial[paramName]'.format(paramName))
    
    for thisUpperLand_trial in UpperLand_trials:
        currentLoop = UpperLand_trials
        # abbreviate parameter names if possible (e.g. rgb = thisUpperLand_trial.rgb)
        if thisUpperLand_trial != None:
            for paramName in thisUpperLand_trial:
                exec('{} = thisUpperLand_trial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Upper_trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        image.setImage(imageU)
        yes_button.setText('Yes')
        no_button.setText('No')
        # keep track of which components have finished
        Upper_trialComponents = [image, text_5, yes_button, no_button]
        for thisComponent in Upper_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Upper_trial" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.started')
                image.setAutoDraw(True)
            
            # *text_5* updates
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.started')
                text_5.setAutoDraw(True)
            
            # *yes_button* updates
            if yes_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                yes_button.frameNStart = frameN  # exact frame index
                yes_button.tStart = t  # local t and not account for scr refresh
                yes_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(yes_button, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'yes_button.started')
                yes_button.setAutoDraw(True)
            if yes_button.status == STARTED:
                # check whether yes_button has been pressed
                if yes_button.isClicked:
                    if not yes_button.wasClicked:
                        yes_button.timesOn.append(yes_button.buttonClock.getTime()) # store time of first click
                        yes_button.timesOff.append(yes_button.buttonClock.getTime()) # store time clicked until
                    else:
                        yes_button.timesOff[-1] = yes_button.buttonClock.getTime() # update time clicked until
                    if not yes_button.wasClicked:
                        continueRoutine = False  # end routine when yes_button is clicked
                        None
                    yes_button.wasClicked = True  # if yes_button is still clicked next frame, it is not a new click
                else:
                    yes_button.wasClicked = False  # if yes_button is clicked next frame, it is a new click
            else:
                yes_button.wasClicked = False  # if yes_button is clicked next frame, it is a new click
            
            # *no_button* updates
            if no_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                no_button.frameNStart = frameN  # exact frame index
                no_button.tStart = t  # local t and not account for scr refresh
                no_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(no_button, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'no_button.started')
                no_button.setAutoDraw(True)
            if no_button.status == STARTED:
                # check whether no_button has been pressed
                if no_button.isClicked:
                    if not no_button.wasClicked:
                        no_button.timesOn.append(no_button.buttonClock.getTime()) # store time of first click
                        no_button.timesOff.append(no_button.buttonClock.getTime()) # store time clicked until
                    else:
                        no_button.timesOff[-1] = no_button.buttonClock.getTime() # update time clicked until
                    if not no_button.wasClicked:
                        continueRoutine = False  # end routine when no_button is clicked
                        None
                    no_button.wasClicked = True  # if no_button is still clicked next frame, it is not a new click
                else:
                    no_button.wasClicked = False  # if no_button is clicked next frame, it is a new click
            else:
                no_button.wasClicked = False  # if no_button is clicked next frame, it is a new click
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Upper_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Upper_trial" ---
        for thisComponent in Upper_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        UpperLand_trials.addData('yes_button.numClicks', yes_button.numClicks)
        if yes_button.numClicks:
           UpperLand_trials.addData('yes_button.timesOn', yes_button.timesOn)
           UpperLand_trials.addData('yes_button.timesOff', yes_button.timesOff)
        else:
           UpperLand_trials.addData('yes_button.timesOn', "")
           UpperLand_trials.addData('yes_button.timesOff', "")
        UpperLand_trials.addData('no_button.numClicks', no_button.numClicks)
        if no_button.numClicks:
           UpperLand_trials.addData('no_button.timesOn', no_button.timesOn)
           UpperLand_trials.addData('no_button.timesOff', no_button.timesOff)
        else:
           UpperLand_trials.addData('no_button.timesOn', "")
           UpperLand_trials.addData('no_button.timesOff', "")
        # the Routine "Upper_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'UpperLand_trials'
    
# completed UpperTrialReps repeats of 'ShowUpperLandtrials_Loop'


# --- Prepare to start Routine "End" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_3.setText('Thank you for participating in the SEAL Landmark Traversal Task')
# keep track of which components have finished
EndComponents = [text_3]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "End" ---
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_3.started')
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.stopped')
            text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "End" ---
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
