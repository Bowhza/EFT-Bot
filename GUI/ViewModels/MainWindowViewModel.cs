using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using System;
using System.Collections.ObjectModel;
using System.Diagnostics;
using System.IO;
using System.Linq;

namespace GUI.ViewModels
{
    public partial class MainWindowViewModel : ViewModelBase
    {
        // Collections
        public ObservableCollection<string>? Maps { get; set; }
        public ObservableCollection<string>? HealthOptions { get; set; }
        public ObservableCollection<string>? SkillOptions { get; set; }

        // Properties
        [ObservableProperty]
        private string selectedMap;

        [ObservableProperty]
        private string selectedHealthOption;

        [ObservableProperty]
        private string selectedSkillOption;

        public MainWindowViewModel() 
        { 
            Maps = new ObservableCollection<string> 
            { 
                "Shoreline", "Woods", "Customs", "Factory", 
                "Interchange", "Lighthouse", "Reserve", 
                "Streets Of Tarkov", "Ground Zero" 
            };
            HealthOptions = new ObservableCollection<string> { "Full heal", "Only heal breaks and bleeds", "Don't heal" };
            SkillOptions = new ObservableCollection<string> { "Endurance/strength" };

            selectedMap = Maps.First();
            selectedHealthOption = HealthOptions.First();
            selectedSkillOption = SkillOptions.First();

            RunBotScriptCommand = new RelayCommand(RunBotScript);
            RunInstallDependeciesCommand = new RelayCommand(RunInstallDependencies);
            RunImageScalerCommand = new RelayCommand(RunImageScaler);
        }

        // RelayCommands
        public RelayCommand RunBotScriptCommand { get; }
        public RelayCommand RunInstallDependeciesCommand { get; }
        public RelayCommand RunImageScalerCommand { get; }


        // Command Methods
        private void RunBotScript()
        {
            string args = $"--map \"{SelectedMap}\" --heal \"{SelectedHealthOption}\" --skill \"{SelectedSkillOption}\"";

            ProcessStartInfo info = new ProcessStartInfo
            {
                FileName = ".venv/Scripts/python.exe",
                Arguments = $"gui_script_run.py {args}",
                CreateNoWindow = false,
            };

            Process process = new Process { StartInfo = info };
            process.Start();
        }


        private void RunInstallDependencies()
        {
            ProcessStartInfo info = new ProcessStartInfo
            {
                FileName = "Install-Dependencies.bat",
                CreateNoWindow = false,
                UseShellExecute = false,
            };

            Process process = new Process { StartInfo = info };
            process.Start();
        }

        private void RunImageScaler()
        {
            // Get the absolute path of the Python executable in the .venv
            string pythonExePath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, @".venv\Scripts\python.exe");

            // Get the absolute path of the Python script
            string scriptPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, @"tools\image_scale.py");

            ProcessStartInfo info = new ProcessStartInfo
            {
                FileName = pythonExePath,
                Arguments = scriptPath,
                WorkingDirectory = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, @"tools"),
                CreateNoWindow = false,
            };

            Process process = new Process { StartInfo = info };
            process.Start();
        }
    }
}
