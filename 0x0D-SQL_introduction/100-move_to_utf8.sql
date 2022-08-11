-- This script converts hbtn_0c_0 database to
-- UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

-- ALTER the database with modified constraints
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- cd/use the database
USE hbtn_0c_0;

-- ALTER the table with modified constraints
ALTER TABLE first_table
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- ALTER the column with modified constraints
ALTER TABLE first_table
MODIFY name VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
