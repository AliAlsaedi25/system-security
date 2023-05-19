#include <iostream>
using namespace std;


typedef struct {
 unsigned int uid; // owner id
 unsigned int gid; // group id
 unsigned char u; // owner's permission
 unsigned char g; // group's permission
 unsigned char o; // other's permission
} Permission;

int getPermission(int f){
    return 5;
}



int accesscheck(unsigned int uid, unsigned int gid, unsigned int p, int f) {
    Permission new_user  = getPermission(f);

    if (uid == new_user.uid) {
        // Check against owner's permission
        if (new_user.u == p) {
            // if it is the same as the owner's permission i will accept
            return 1;
        }else {
            // if it is not the same as the owners permission i will deny 
            return 0;
        }
    } else if (gid == new_user.gid) {
        // Check against group's permission
        if (new_user.g == p ){
            // if it is the same as the group's permission i will accept
            return 1;
        }else {
            // if it is not the same as the groups permission i will deny 
            return 0;
        }
    } else {
        // Check against other's permission
        if (new_user.o == p) {
            // if it is the same as the others permission i will accept
            return 1;
        }else {
            // if it is not the same as the others permission i will deny 
            return 0;
        }

    }
    return 0;
}



int accesscheck(unsigned int uid, unsigned int gid, unsigned int p, int f) {

    Permission new_user  = getPermission(f); 

    // Check against owners ID
    if (uid == new_user.uid) {
        // checking against the owner's permission 
        if ((new_user.u & p) == p) {
            // if it is the same as the owner's permission i will accept
            return 1;
        }
    // Check against group's ID
    } else if (gid == new_user.gid) { 
        // checking against the group's permission 
        if ((new_user.g & p) == p ){
            // if it is the same as the group's permission i will accept
            return 1;
        }
    // Check against other's permission
    } else if ((new_user.o & p ) == p) {
        // if it is the same as the permission i will grant access 
        return 1;
    }
    else {
        //otherwise deny 
        return 0;
    }
    return 0;
}
