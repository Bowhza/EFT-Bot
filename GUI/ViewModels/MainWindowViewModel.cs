using CommunityToolkit.Mvvm.ComponentModel;
using System.Collections.ObjectModel;
using System.Linq;

namespace GUI.ViewModels
{
    public partial class MainWindowViewModel : ViewModelBase
    {
        public ObservableCollection<string>? Maps { get; set; }
        public ObservableCollection<string>? HealthOptions { get; set; }
        public ObservableCollection<string>? SkillOptions { get; set; }

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
            HealthOptions = new ObservableCollection<string> { "Full Heal", "Only Heal Breaks and Bleeds", "Don't Heal" };
            SkillOptions = new ObservableCollection<string> { "Endurance/Strength" };

            selectedMap = Maps.First();
            selectedHealthOption = HealthOptions.First();
            selectedSkillOption = SkillOptions.First();
        }
    }
}
