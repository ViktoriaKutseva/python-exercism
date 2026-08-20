static class Appointment
{
    public static DateTime Schedule(string appointmentDateDescription)
    {
        DateTime date1 = DateTime.Parse(appointmentDateDescription);
        return date1;
    }
    public static bool HasPassed(DateTime appointmentDate)
    {
        if (appointmentDate < DateTime.Now)
        {
            return true;
        }
        return false;
    }

    public static bool IsAfternoonAppointment(DateTime appointmentDate)
    {
        if (appointmentDate.Hour >= 12 && appointmentDate.Hour < 18)
        {
            return true;
        }
        return false;
    }

    public static string Description(DateTime appointmentDate)
    {
        var showDateTime = $"You have an appointment on {appointmentDate}.";
        return showDateTime;
    }

    public static DateTime AnniversaryDate()
    {
        return new DateTime(DateTime.Now.Year, 9, 15);
    }
}

