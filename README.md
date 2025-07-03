# 💰 Personal Finance Tracker

A comprehensive Django web application for managing personal finances with advanced reporting, budgeting, and transaction tracking capabilities.

## 🚀 Features

### 📊 **Smart Financial Management**
- **Transaction Tracking**: Record income and expenses with detailed categorization
- **Budget Management**: Set and monitor budgets by category with real-time tracking
- **Advanced Reporting**: Interactive date filtering with customizable time periods
- **Financial Analytics**: Monthly trends, spending patterns, and budget analysis

### 🎯 **User Experience**
- **Responsive Design**: Modern, mobile-friendly interface built with Tailwind CSS
- **User Authentication**: Secure login/registration with profile management
- **Data Export**: Export financial reports to CSV format
- **Real-time Updates**: Live data updates and instant feedback

### 📈 **Reporting & Analytics**
- **Date Range Filtering**: Quick filters (7 days, 30 days, this month, etc.) and custom date ranges
- **Clickable Monthly Trends**: Click any month to filter reports to that period
- **Budget Analysis**: Track spending vs. budget with visual status indicators
- **Category Breakdown**: Top spending categories and transaction counts
- **Net Income Tracking**: Real-time calculation of income vs. expenses

### 🏦 **Financial Tools**
- **Multiple Payment Methods**: Track transactions by payment method (cash, card, etc.)
- **Category Management**: Custom categories for income and expenses
- **Savings Goals**: Set and track savings targets
- **Card/Account Management**: Organize multiple financial accounts

## 🛠️ Technology Stack

- **Backend**: Django 5.2.3 (Python)
- **Frontend**: HTML5, CSS3, JavaScript, Tailwind CSS
- **Database**: SQLite (development), PostgreSQL ready
- **Authentication**: Django's built-in user authentication
- **File Handling**: Django's file upload system for profile images
- **Deployment**: Ready for production deployment

## 📋 Requirements

- Python 3.8+
- Django 5.2.3
- Additional packages listed in `requirements.txt`

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/personal_finance_tracker.git
   cd personal_finance_tracker
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Visit the application**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Register a new account or login

## 📱 Key Features in Action

### **Smart Date Filtering**
- Filter reports by any time period (7 days to 1 year)
- Click on monthly trend rows to instantly filter to that month
- Custom date range picker for precise analysis

### **Budget Management**
- Set budgets by category
- Real-time tracking of spending vs. budget
- Visual indicators for over/under budget status

### **Transaction Management**
- Add, edit, and delete transactions
- Categorize income and expenses
- Track payment methods
- Detailed transaction history

### **Financial Reports**
- Comprehensive financial summaries
- Export data to CSV format
- Interactive charts and tables
- Category-wise spending analysis

## 🔒 Security Features

- User authentication and authorization
- Per-user data isolation
- Secure password handling
- CSRF protection
- SQL injection prevention

## 📊 Screenshots

![FinTrack-03-07-2025_19_14](https://github.com/user-attachments/assets/c2740137-9742-48ae-ad29-75e18af9fc26)
![FinTrack-03-07-2025_19_14 (3)](https://github.com/user-attachments/assets/cd478a07-1950-4c68-9712-640a70172de8)
![FinTrack-03-07-2025_19_14 (2)](https://github.com/user-attachments/assets/9d1ed771-23aa-4a86-891c-4163ac3f74f6)
![FinTrack-03-07-2025_19_14 (1)](https://github.com/user-attachments/assets/ba868739-f2e5-4f7a-887d-f61457c5fffe)
![Screenshot_20250703-191327](https://github.com/user-attachments/assets/97a5d899-4475-4cc4-b6cf-46d97f304c2d)
![Screenshot_20250703-191315](https://github.com/user-attachments/assets/8eade338-d1e4-40ce-bdbe-149952fe5401)
![Screenshot_20250703-191303](https://github.com/user-attachments/assets/5acfa9e5-919c-4dbf-b04a-8d8708ab3d5c)


## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Django framework
- Styled with Tailwind CSS
- Icons from various open-source icon libraries

## 📞 Support

If you have any questions or need support, please open an issue on GitHub.

---

**Made with ❤️ for better financial management** 
