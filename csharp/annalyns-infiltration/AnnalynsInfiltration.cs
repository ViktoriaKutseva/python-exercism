using Microsoft.VisualBasic;

static class QuestLogic
{
    public static bool CanFastAttack(bool knightIsAwake)
    {
        if (knightIsAwake)
        {
            return false;
        }
        return true;
    }

    public static bool CanSpy(bool knightIsAwake, bool archerIsAwake, bool prisonerIsAwake)
    {
        if (knightIsAwake == false && archerIsAwake == false && prisonerIsAwake == false)
        {
            return false;
        }
        return true;
    }

    public static bool CanSignalPrisoner(bool archerIsAwake, bool prisonerIsAwake)
    {
        if (archerIsAwake == false && prisonerIsAwake)
        {
            return true;
        }
        return false;
    }

    public static bool CanFreePrisoner(bool knightIsAwake, bool archerIsAwake, bool prisonerIsAwake, bool petDogIsPresent)
    {
        if (((knightIsAwake || knightIsAwake == false) && archerIsAwake == false && (prisonerIsAwake || prisonerIsAwake == false) && petDogIsPresent) || (knightIsAwake == false && archerIsAwake == false && prisonerIsAwake))
        {
            return true;
        }
        return false;
    }
}
