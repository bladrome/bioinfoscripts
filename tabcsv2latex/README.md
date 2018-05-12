# csv 2 latex tabular

## samtools
change
```
$ git diff
diff --git a/bam_tview.c b/bam_tview.c
index 206ac8b..6503b80 100644
--- a/bam_tview.c
+++ b/bam_tview.c
@@ -62,9 +62,11 @@ int base_tv_init(tview_t* tv, const char *fn, const char *fn_fa,
 {
     assert(tv!=NULL);
     assert(fn!=NULL);
-    tv->mrow = 24; tv->mcol = 80;
+    /*tv->mrow = 24; tv->mcol = 80;*/
+    tv->mrow = 24; tv->mcol = 500;
     tv->color_for = TV_COLOR_MAPQ;
-    tv->is_dot = 1;
+    /*tv->is_dot = 1;*/
+    tv->is_dot = 0;
 
     tv->fp = sam_open_format(fn, "r", fmt);
     if(tv->fp == NULL)
```
