using Avalonia;
using Avalonia.Controls;
using Avalonia.Controls.Chrome;
using Avalonia.Input;
using Avalonia.Interactivity;
using GUI.ViewModels;
using System;
using System.Diagnostics;

namespace GUI.Views
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            WindowStartupLocation = WindowStartupLocation.CenterScreen;
            DataContext = new MainWindowViewModel();
        }

        private void Window_PointerPressed(object? sender, PointerPressedEventArgs e)
        {
            // Check if the left mouse button was pressed
            if (e.GetCurrentPoint(CustomTitleBar).Properties.IsLeftButtonPressed)
            {
                // Start dragging the window
                this.BeginMoveDrag(e);
            }
        }

        private void Close_Click(object? sender, RoutedEventArgs e)
        {
            Close();
        }

        private void Minimize_Click(object? sender, RoutedEventArgs e)
        {
            WindowState = WindowState.Minimized;
        }
    }
}