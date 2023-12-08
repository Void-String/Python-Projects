^j::

ScreenTopLeftX := 16
ScreenTopLeftY := 16
ScreenBottomRightX := 1366
ScreenBottomRightY := 768


Loop {
	Loop{
		ImageSearch, FoundPartyScreenX, FoundPartyScreenY, %ScreenTopLeftX%, %ScreenTopLeftY%, %ScreenBottomRightX%, %ScreenBottomRightY%, *50, .\partyscreen.png
		if(FoundPartyScreenX > 0)
		{
			Click, %FoundPartyScreenX% %FoundPartyScreenY%
			break
		}
		else
		{
			break
		}
		Sleep 100
	}
	Loop{
		ImageSearch, FoundStartScreenX, FoundStartScreenY, %ScreenTopLeftX%, %ScreenTopLeftY%, %ScreenBottomRightX%, %ScreenBottomRightY%, *50, .\startbutton.png
		if(FoundStartScreenX > 0)
		{
			Click, %FoundStartScreenX% %FoundStartScreenY%
			break
		}
		else
		{
			break
		}
		Sleep 100
	}
	;If story screen is active then click skip
	Loop{
		ImageSearch, FoundStoryScreenX, FoundStoryScreenY, %ScreenTopLeftX%, %ScreenTopLeftY%, %ScreenBottomRightX%, %ScreenBottomRightY%, *50, .\storyscreen.png
		if(FoundStoryScreenX > 0)
		{
			Click, 658 625
			break
		}
		else
		{
			break
		}
		Sleep 100
	}
	Loop{
		ImageSearch, FoundYesScreenX, FoundYesScreenY, %ScreenTopLeftX%, %ScreenTopLeftY%, %ScreenBottomRightX%, %ScreenBottomRightY%, *50, .\yesbutton.png
		if(FoundYesScreenX > 0)
		{
			Click, %FoundYesScreenX% %FoundYesScreenY%
			break
		}
		else
		{
			break
		}
		Sleep 100
	}
	Loop{
		ImageSearch, FoundBattleScreenX, FoundBattleScreenY, %ScreenTopLeftX%, %ScreenTopLeftY%, %ScreenBottomRightX%, %ScreenBottomRightY%, *50, .\battlebutton.png
		if(FoundBattleScreenX > 0)
		{
			Click, %FoundBattleScreenX% %FoundBattleScreenY%
			Sleep 1000
			Click, 658 625
			break
		}
		else
		{
			break
		}
		Sleep 100
	}
	Loop{
		ImageSearch, FoundCompleteScreenX, FoundCompleteScreenY, %ScreenTopLeftX%, %ScreenTopLeftY%, %ScreenBottomRightX%, %ScreenBottomRightY%, *50, .\stagecomplete.png
		if(FoundCompleteScreenX > 0)
		{
			Click, %FoundCompleteScreenX% %FoundCompleteScreenY%
			break
		}
		else
		{
			break
		}
		Sleep 100
	}
	
	;If bonus screen is active then click no
	Loop{
		ImageSearch, FoundNoScreenX, FoundNoScreenY, %ScreenTopLeftX%, %ScreenTopLeftY%, %ScreenBottomRightX%, %ScreenBottomRightY%, *50, .\nobutton.png
		if(FoundNoScreenX > 0)
		{
			Click, %FoundNoScreenX% %FoundNoScreenY%
			break
		}
		else
		{
			break
		}
		Sleep 100
	}
	Loop{
		ImageSearch, FoundNextScreenX, FoundNextScreenY, %ScreenTopLeftX%, %ScreenTopLeftY%, %ScreenBottomRightX%, %ScreenBottomRightY%, *50, .\nextstage.png
		if(FoundNextScreenX > 0)
		{
			Click, %FoundNextScreenX% %FoundNextScreenY%
			break
		}
		else
		{
			break
		}
		Sleep 100
	}
	Loop{
		ImageSearch, FoundBossScreenX, FoundBossScreenY, %ScreenTopLeftX%, %ScreenTopLeftY%, %ScreenBottomRightX%, %ScreenBottomRightY%, *50, .\skipboss.png
		if(FoundBossScreenX > 0)
		{
			Click, %FoundBossScreenX% %FoundBossScreenY%
			break
		}
		else
		{
			break
		}
		Sleep 100
	}
	Sleep 1000
}