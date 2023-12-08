^s::Pause
^j::

ScreenTopLeftX := 16
ScreenTopLeftY := 16
ScreenBottomRightX := 1366
ScreenBottomRightY := 768

Loop {
	Loop{
		ImageSearch, ZeroAffectionX, ZeroAffectionY, %ScreenTopLeftX%, %ScreenTopLeftY%, %ScreenBottomRightX%, %ScreenBottomRightY%, *50, .\ZeroAffection.png
		if(ZeroAffectionX > 0)
		{
			Click, %ZeroAffectionX% %ZeroAffectionY%
			break
		}
		else
		{
			break
		}
		Sleep 500
	}
	Loop{
		ImageSearch, SendGiftX, SendGiftY, %ScreenTopLeftX%, %ScreenTopLeftY%, %ScreenBottomRightX%, %ScreenBottomRightY%, *50, .\SendGift.png
		if(SendGiftX > 0)
		{
			Click, %SendGiftX% %SendGiftY%
			break
		}
		else
		{
			break
		}
		Sleep 500
	}
	Loop{
		ImageSearch, GiveGiftX, GiveGiftY, %ScreenTopLeftX%, %ScreenTopLeftY%, %ScreenBottomRightX%, %ScreenBottomRightY%, *50, .\GiveGift.png
		if(GiveGiftX > 0)
		{
			Click, %GiveGiftX% %GiveGiftY%
			break
		}
		else
		{
			break
		}
		Sleep 500
	}
	Loop{
		ImageSearch, ConfirmX, ConfirmY, %ScreenTopLeftX%, %ScreenTopLeftY%, %ScreenBottomRightX%, %ScreenBottomRightY%, *50, .\Confirm.png
		if(ConfirmX > 0)
		{
			Click, %ConfirmX% %ConfirmY%
			break
		}
		else
		{
			break
		}
		Sleep 500
	}
	Loop{
		ImageSearch, YesX, YesY, %ScreenTopLeftX%, %ScreenTopLeftY%, %ScreenBottomRightX%, %ScreenBottomRightY%, *50, .\Yes.png
		if(YesX > 0)
		{
			Click, %YesX% %YesY%
			break
		}
		else
		{
			break
		}
		Sleep 500
	}
	Loop{
		ImageSearch, DialogueX, DialogueY, %ScreenTopLeftX%, %ScreenTopLeftY%, %ScreenBottomRightX%, %ScreenBottomRightY%, *50, .\Dialogue.png
		if(DialogueX > 0)
		{
			Click, %DialogueX% %DialogueY%
			break
		}
		else
		{
			break
		}
		Sleep 500
	}
	Loop{
		ImageSearch, skipDialogueX, skipDialogueY, %ScreenTopLeftX%, %ScreenTopLeftY%, %ScreenBottomRightX%, %ScreenBottomRightY%, *50, .\skipDialogue.png
		if(skipDialogueX > 0)
		{
			Click, 655 702
			break
		}
		else
		{
			break
		}
		Sleep 500
	}
	Loop{
		ImageSearch, confirmSkipX, confirmSkipY, %ScreenTopLeftX%, %ScreenTopLeftY%, %ScreenBottomRightX%, %ScreenBottomRightY%, *50, .\confirmSkip.png
		if(confirmSkipX > 0)
		{
			Click, %confirmSkipX% %confirmSkipY%
			break
		}
		else
		{
			break
		}
		Sleep 500
	}
	Loop{
		ImageSearch, confirmRewardsX, confirmRewardsY, %ScreenTopLeftX%, %ScreenTopLeftY%, %ScreenBottomRightX%, %ScreenBottomRightY%, *50, .\confirmRewards.png
		if(confirmRewardsX > 0)
		{
			isDefaultScreen = 0
			Click, %confirmRewardsX% %confirmRewardsY%
			break
		}
		else
		{
			break
		}
		Sleep 500
	}
	Loop{
		ImageSearch, ReturnX, ReturnY, %ScreenTopLeftX%, %ScreenTopLeftY%, %ScreenBottomRightX%, %ScreenBottomRightY%, *50, .\Return.png
		if(ReturnX > 0 && isDefaultScreen == 0)
		{
			isDefaultScreen = 1
			Click, %ReturnX% %ReturnY%
			break
		}
		else
		{
			break
		}
		Sleep 500
	}
	Sleep 500
}