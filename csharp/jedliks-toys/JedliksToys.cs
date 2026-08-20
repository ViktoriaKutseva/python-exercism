using System.IO.Pipes;
using System.Runtime.CompilerServices;
using Microsoft.VisualBasic;

class RemoteControlCar
{
    private int _distance;
    private int _battery = 100;
    public static RemoteControlCar Buy()
    {
        var car = new RemoteControlCar();
        return car;
    }

    public string DistanceDisplay()
    {
        return $"Driven {_distance} meters";
    }

    public string BatteryDisplay()
    {
        if (_battery > 0)
        {
            return $"Battery at {_battery}%";
        }
        return "Battery empty";

    }

    public void Drive()
    {
        _battery -= 1;
        if (_battery == 0)
        {
            _distance +=0;
        }
        else
        {
            _distance += 20;
        }
    }
}
