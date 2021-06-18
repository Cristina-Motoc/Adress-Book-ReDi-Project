
#Import function to clear screen
import os


#Define Variables
contacts_list = []
exit_application = False


#Importing Address Book

#Read content of contacts file
if os.path.isfile('contacts_file.txt') == True:
	with open('contacts_file.txt', 'r') as file_content:
	#loop through each line in contacts file
		for line in file_content:
			#create contact as a list from each line
			contact = line.strip().split(';') 
			#add each contact to contact list variable
			contacts_list.append(contact)


#Clear screen
os.system('cls')


#Address book logic
while exit_application != True:
			
			#Reset contact found counter
			contact_found=0
			
			#Print main menu
			print('Address Book Main Menu:')
			print('-----------------------------')
			print('Press 1 to List Contact')
			print('Press 2 to Edit Contact')
			print('Press 3 to Add Contact')
			print('Press 4 to Delete Contact')
			print('Press 5 to Exit Address Book')
			user_input = int(input())

			#Verify user input is valid
			while user_input < 1 or user_input > 5 :
				print ('\nPlease enter a valid option (1 to 5).')
				user_input = int(input())
				
			 
			#Starting List Contact command
			if user_input == 1:
				#Clear screen
				os.system('cls')
				print('Listing existing contact.\n')
				#Ask user to input search string
				print('Please enter a name:')
				input_name = str(input())
				#Search address book for input name
				for contact in contacts_list:
					if contact[0].lower().find(input_name.lower()) !=  -1 or contact[1].lower().find(input_name.lower()) !=  -1:
						print('\nContact Name: ',contact[0],contact[1])
						print('  address:  ',contact[2])
						print('  email:    ',contact[3])
						print('  phone nr: ',contact[4])
						contact_found=1
				#Display warning if no match found		
				if contact_found != 1:
					print('\nNo matching contact found!')
					
					
			#Starting Edit Contacts command
			if user_input == 2:
				#Clear screen
				os.system('cls')
				print('Editing contact.')
				print('\nPlease enter the First name of contact you want to edit:')
				edit_firstname = str(input())
				print('Please enter the Last name of contact you want to edit:')
				edit_lastname = str(input())
				#Search address book for contact full name
				for contact in contacts_list:
					if contact[0].lower().find(edit_firstname.lower()) !=  -1 and contact[1].lower().find(edit_lastname.lower()) !=  -1:
						#Display contact that will be edited
						print('\nContact Name: ',contact[0],contact[1])
						print('  address:  ',contact[2])
						print('  email:    ',contact[3])
						print('  phone nr: ',contact[4])
						#Prompt user for new values
						print('\nPlease enter new First name value:')
						edit_newfirstname = str(input())
						print('Please enter new Last name value:')
						edit_newlastname = str(input())
						print('Please enter new address value:')
						edit_newaddress = str(input())
						print('Please enter new e-mail value:')
						edit_newemail = str(input())
						print('Please enter new phone number value:')
						edit_newphone = str(input())
						#Save contacts_list position of current contact
						current_index = contacts_list.index(contact)
						#Update contact in address book
						contacts_list[current_index]=[edit_newfirstname,edit_newlastname,edit_newaddress,edit_newemail,edit_newphone]
						print('\nContact details updated.')
						contact_found = 1
				#Display warning if no match found		
				if contact_found != 1:
					print('\nNo matching contact found!')
					
											   
			#Starting Add new contact command 
			if user_input == 3:
				#Clear screen
				os.system('cls')
				print('Adding new contact.\n')
				#Ask user for contact details
				print('Please enter First name of the contact.')
				first_name = str(input())
				print('Please enter Last name of the contact.')
				last_name = str(input())
				print('Please enter the address.')
				inserted_address = str(input())
				print('Please enter the email address.')
				inserted_email = str(input())
				print('Please enter the telephone number.')
				inserted_telephone_number = str(input())
				#Add new contact to address book
				contacts_list.append([first_name,last_name,inserted_address,inserted_email,inserted_telephone_number])
				print('\nNew Contact added.')
				
			
			#Starting Remove contact command
			if user_input == 4:
				#Clear screen
				os.system('cls')
				print('Removing contact.\n')
				print('Please enter the First name of contact you want to remove.')
				remove_firstname = str(input())
				print('Please enter the Last name of contact you want to remove.')
				remove_lastname = str(input())
				#Search address book for contact full name
				for contact in contacts_list:
					if contact[0].lower().find(remove_firstname.lower()) !=  -1 and contact[1].lower().find(remove_lastname.lower()) !=  -1:
						#Display contact that will be removed
						print('\nContact Name: ',contact[0],contact[1])
						print('  address:  ',contact[2])
						print('  email:    ',contact[3])
						print('  phone nr: ',contact[4])
						#Deleting contact
						contacts_list.remove(contact)
						print('\nContact deleted from Address Book.')
						contact_found = 1
				#Display warning if no match found		
				if contact_found != 1:
					print('\nNo matching contact found!')		

			 
			#Starting Exit application command
			if user_input == 5:
				exit_application = True
				
			
			#Pause script to display results before going back to main menu
			if user_input != 5:
				input("\n\n\n\n\nPress Enter to go back to Main Menu...")
			
			#Clear screen
			os.system('cls')


#Saving contact variable to file

#open contacts_file to write
file_content = open('contacts_file.txt', 'w')
#For each contact in contacts_list variable add a new line to contacts_file
for contact in contacts_list:
	file_content.write(contact[0] + ';')
	file_content.write(contact[1] + ';')
	file_content.write(contact[2] + ';')
	file_content.write(contact[3] + ';')
	file_content.write(contact[4] + '\n')
#Save file
file_content.close()



 