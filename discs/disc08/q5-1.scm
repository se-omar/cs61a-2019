;; Write a function which takes two lists and concatenates them.
;; Notice that simply calling (cons a b) would not work because it will create a
;; deep list. Do not call the builtin procedure append, which does the same thing as
;; my-append.
(define (my-append a b)
  (cond
    ((null? a) b)
    ((null? (cdr a)) (cons (car a) b))
    (else
      (cons (car a) (my-append (cdr a) b))
    )
  )
)
