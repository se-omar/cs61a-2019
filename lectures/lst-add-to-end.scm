(define (add-to-end lst x)
  (cond
    ((null? lst) (cons x '()))
    (else 
      (cons (car lst) (add-to-end (cdr lst) x))
      )
  )
)
