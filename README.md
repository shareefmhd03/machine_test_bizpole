# machine_test_bizpole
# Project Name

This is a CRUD application developed using Django and HTML. It allows end-users to register, login, and choose an activity type. Users can view and edit activities associated with their account, while administrators have additional permissions to view and delete activities.

## Installation

1. Clone the repository to your local machine:


2. Change to the project directory:


3. Create a virtual environment:


4. Activate the virtual environment:

- For Windows:

  ```
  env\Scripts\activate
  ```

- For Unix or Linux:

  ```
  source env/bin/activate
  ```

5. Install the project dependencies:


6. Run the migrations to set up the database:


7. Start the development server:


8. Access the application in your web browser at `http://localhost:8000`.

## URLs

- Register: `activity/register`
- Login: `activity/login`
- Activity Listing: `activity/activities`
- Fetch More Activities: `activity/fetch-activities`
- Edit Activity: `activity/edit/<activity_id>/`
- Admin : `/admin`

## Third Party services
- Recaptcha - for captcha verification
- Maelys - email service
