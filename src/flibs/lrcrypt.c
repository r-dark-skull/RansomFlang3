#define _OPEN_SYS_ITOA_EXT
#include <stdio.h>
#include <gcrypt.h>
#include <string.h>
#include <stdlib.h>

/* Generate new key pair of set size */

void get_new_pair_key(int key_size, gcry_sexp_t *pub_key, gcry_sexp_t *pri_key){

    char *buffer_def = malloc(50);
    gcry_sexp_t key_spec, key;

    // formatting key, size and specification
    sprintf(buffer_def, "(genkey (rsa (nbits 4:%d)))", key_size);

    int rc = gcry_sexp_new(&key_spec, buffer_def, 0, 1);
    if(rc){
        printf("Failed to generate Key, Exiting Program..!");
        exit(1);
    }
    
    // generating key
    rc = gcry_pk_genkey(&key, key_spec);
    gcry_sexp_release(key_spec);
    if(rc){
        printf("Failed to generate Key, Exiting Program..!");
        exit(1);
    }

    *pub_key = gcry_sexp_find_token(key, "public-key", 0);
    *pri_key = gcry_sexp_find_token(key, "private-key", 0);
}



int main(){

    gcry_sexp_t *pub_key, *pri_key;
    get_new_pair_key(4096, &pub_key, &pri_key);

    show_sexp("PUBLIC KEY: ", pub_key);
    show_sexp("PRIVATE KEY: ", pri_key);
    

    return 0;
}
