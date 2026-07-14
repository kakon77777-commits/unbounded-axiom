import Std

namespace FormalKneser

theorem smoke : 1 + 1 = 2 := by
  rfl

theorem decideSmoke : (List.range 9).length = 9 := by
  decide

end FormalKneser
