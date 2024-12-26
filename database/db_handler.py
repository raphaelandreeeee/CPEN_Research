import sqlite3


class DatabaseHandler:
    def __init__(self, db_name=r"database.db"):
        self.db_name = db_name

    def create_connection(self):
        """Create and return a database connection."""
        return sqlite3.connect(self.db_name)

    def create_class(self, class_name: str) -> None:
    
        try:
            with self.create_connection() as connection:
                cursor = connection.cursor()

                cursor.execute(f"""
                    CREATE TABLE IF NOT EXISTS {class_name} (
                        attendance INTEGER, 
                        first_name TEXT NOT NULL, 
                        last_name TEXT NOT NULL, 
                        id_number TEXT NOT NULL 
                    )                 
                """)

                connection.commit()

        except sqlite3.Error as e:
            print(f"Error creating class: {e}")

    def remove_class(self, class_name: str) -> None:
        
        try:
            with self.create_connection() as connection:
                cursor = connection.cursor()

                cursor.execute(f"""
                    DROP TABLE {class_name}
                """)
                
                connection.commit()

        except sqlite3.Error as e:
            print(f"Error deleting class: {e}")

    def add_student(self, first_name: str, last_name: str, id_number: str, class_name: str, attendance=0):
        
        try:
            with self.create_connection() as connection:
                cursor = connection.cursor()

                cursor.execute(f"""
                    SELECT id_number
                    FROM {class_name}
                """)

                ids = cursor.fetchall()

                for row in ids:
                    if id_number in row:

                        print(f"Error adding student: ID already exists.")
                        return

                cursor.execute(f"""
                    INSERT INTO {class_name} (
                        attendance, 
                        first_name, 
                        last_name, 
                        id_number
                    ) VALUES (?, ?, ?, ?)
                """, (attendance, first_name, last_name, id_number))

                connection.commit()

        except sqlite3.Error as e:
            print(f"Error adding student: {e}")

    def remove_student(self, id_number: str, class_name: str) -> None:
        
        try:
            with self.create_connection() as connection:
                cursor = connection.cursor()

                cursor.execute(f"""
                    DELETE FROM {class_name} 
                    WHERE id_number = ?
                """, (id_number, ))

                connection.commit()

        except sqlite3.Error as e:
            print(f"Error removing student: {e}")

    def search_student(self, id_number, class_name):
        
        try:
            with self.create_connection() as connection:
                cursor =  connection.cursor()

                cursor.execute(f"""
                    SELECT first_name, last_name
                    FROM {class_name}
                    WHERE id_number = ?
                """, (id_number, ))

                return cursor.fetchone()
        
        except sqlite3.Error as e:
            print(f"Error searching student: {e}")

    def check_class_attendance(self, class_name) -> int:
        
        try:
            with self.create_connection() as connection:
                cursor = connection.cursor()

                cursor.execute(f"""
                    SELECT attendance
                    FROM {class_name}
                """)

                return min(cursor.fetchall())

        except sqlite3.Error as e:
            print(f"Error checking attendances: {e}")

    def check_student_attendance(self, id_number: str, class_name: str) -> int:
        
        try:
            with self.create_connection() as connection:
                cursor = connection.cursor()

                cursor.execute(f"""
                    SELECT attendance
                    FROM {class_name}
                    WHERE id_number = ?
                """, (id_number, ))

                connection.commit()

                return cursor.fetchone()

        except sqlite3.Error as e:
            print(f"Error checking student's attendance: {e}")

    def increment_student_attendance(self, id_number: str, class_name: str, increment=1) -> None:

        try:
            with self.create_connection() as connection:
                cursor = connection.cursor()

                cursor.execute(f"""
                    SELECT attendance
                    FROM {class_name}
                    WHERE id_number = ?
                """, (id_number, ))

                attendance = cursor.fetchone()
                attendance = attendance[0] + increment

                cursor.execute(f"""
                     UPDATE {class_name} 
                     SET attendance = {attendance} 
                     WHERE id_number = ?
                """, (id_number, ))
                
                connection.commit()

        except sqlite3.Error as e:
            print(f"Error incrementing student's attendance: {e}")


if __name__ == '__main__':
    database = DatabaseHandler()

    database.create_class("CPEN")

    database.add_student("raphael", "lontoc", "abc123", "CPEN")
    database.add_student("raphael", "lontoc", "abc123", "CPEN")
    database.add_student("james", "felices", "abc124", "CPEN")

    print(database.search_student("abc123", "CPEN"))

    print(database.check_class_attendance("CPEN"))

    print(database.check_student_attendance("abc123", "CPEN"))

    database.increment_student_attendance("abc123", "CPEN")
