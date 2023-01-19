;; Write a function that takes an element x and a non-negative integer n, and returns
;; a list with x repeated n times.

(define (replicate x n)
  (cond 
    ((= n 0) '())
    (else (cons x (replicate x (- n 1))))
  )
)
