# If Santa, Then Christmas

[doc](https://docs.google.com/document/d/1cIHd_YQ_PHhkUPMrEDWAIfQFb9M9ge3OFr22HHaHQOU/edit?tab=t.0)

1. what is the value of local_8h before the end of the main function?
   Ans:9
   1. set break at mv at the end
   2. `dc` to it and `pxv @ <addr>`

2. what is the value of local_4h before the end of the main function?
   Ans:2
   ` pxv @ rbp-0x4`
