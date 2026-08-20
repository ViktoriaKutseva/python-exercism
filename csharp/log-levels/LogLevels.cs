static class LogLine
{
    public static string Message(string logLine) => logLine.Split("]: ")[1].Trim();
        // string[] levels = ["[ERROR]:", "[WARNING]:", "[INFO]:"];
        // for (int i = 0; i < levels.Length; i++)
        // {
        //     string newString = logLine.Replace(levels[i], "");
        //     if (newString.Length < logLine.Length)
        //     {
        //         return newString.Trim();
        //     }
        // }
        // return "";

    public static string LogLevel(string logLine) => logLine.Split("]")[0].ToLower().Trim().Substring(1);

    public static string Reformat(string logLine) => $"{Message(logLine)} ({LogLevel(logLine)})";

}
