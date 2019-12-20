-- meta=init_sections=create_tables,create_idx

-- name=create_idx
create index person_name on person(name);

-- name=create_tables
create table person (
       uid serial primary key,
       name text,
       age int);

-- name=destroy
drop table person;

-- name=insert_person
insert into person (name, age) values (%s, %s) returning person.uid;

-- name=select_people; note that the order is needed for the unit tests only
select name, age, uid as id
       from person
       order by name;

-- name=select_people_by_id
select name, age, uid as id from person where uid = %s;

-- name=update_person
update person set name = %s, age = %s where uid = %s returning uid;

-- name=delete_person
delete from person where uid = %s returning uid;

-- name=people_ids; note that the order is needed for the unit tests only
select uid from person order by uid;

-- name=select_person_exists_by_id
select count(*) from person where uid = %s;

-- name=people_count
select count(*) from person;
